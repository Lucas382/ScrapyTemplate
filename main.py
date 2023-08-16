import sqlite3


def main():
    try:
        banco = sqlite3.connect('bookscraper/books.db')
        cursor = banco.cursor()
        data = cursor.execute("SELECT *  FROM books LIMIT 10")

        for d in data:
            print(d)

        banco.close()

    except sqlite3.Error as e:
        print("Error accessing the database:", e)


if __name__ == '__main__':
    main()
