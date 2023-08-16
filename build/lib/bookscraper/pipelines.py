# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3


class BookscraperPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings
        field_names = adapter.field_names()

        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                if isinstance(adapter[field_name], tuple):
                    adapter[field_name] = value[0].strip()
                else:
                    adapter[field_name] = value.strip()
            else:
                value = adapter.get(field_name)
                adapter[field_name] = str(value[0])

        # Category & Product Type --> switch to lowercase
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        # Price --> convert to float
        price_keys = ['price_excl_tax', 'price_incl_tax', 'tax', 'price']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '')
            adapter[price_key] = float(value)

        # Availability --> extract number of books in stock (removing strings)
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_string = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_string[0])

        # Reviews --> convert string to int
        num_reviews_string = adapter.get('num_reviews')
        adapter['num_reviews'] = int(num_reviews_string)

        # Stars --> covert text to number
        stars_string = adapter.get('stars')
        split_stars_array = stars_string.split(' ')
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == "zero":
            adapter['stars'] = 0
        elif stars_text_value == "one":
            adapter['stars'] = 1
        elif stars_text_value == "two":
            adapter['stars'] = 2
        elif stars_text_value == "three":
            adapter['stars'] = 3
        elif stars_text_value == "four":
            adapter['stars'] = 4
        elif stars_text_value == "five":
            adapter['stars'] = 5

        return item


class SaveToSQLitePipeline:

    def open_spider(self, spider):
        self.conn = sqlite3.connect('books.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            url TEXT,
            title TEXT,
            upc TEXT,
            product_type TEXT,
            price_excl_tax REAL,
            price_incl_tax REAL,
            tax REAL,
            availability INTEGER,
            num_reviews INTEGER,
            stars REAL,
            category TEXT,
            description TEXT,
            price REAL
        );
        """)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        query = """
            INSERT INTO books (
                url, title, upc, product_type, price_excl_tax, price_incl_tax,
                tax, availability, num_reviews, stars, category, description, price
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            item['url'],
            item['title'],
            item['upc'],
            item['product_type'],
            item['price_excl_tax'],
            item['price_incl_tax'],
            item['tax'],
            item['availability'],
            item['num_reviews'],
            item['stars'],
            item['category'],
            item['description'],
            item['price']
        )

        self.cur.execute(query, values)
        self.conn.commit()
        return item
