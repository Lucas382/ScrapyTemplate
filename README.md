<a name="readme-top"></a>
<aside>
👣 *Passo a passo:*

---
**Instalação e primeiro contato:**

<details>
<summary>Instalação Scrapy</summary>

  -  Criar um novo projeto com ambiente virtual
  -  Abrir terminal e instalar o Scrapy com o comando “pip install Scrapy”
</details>

<details>
<summary>Criar um projeto de Spider</summary>

-  Terminal: “scrapy startproject nomedoprojetoscraper”
</details>

<details>
<summary>Criar uma Spider</summary>

-  Navegar até a pasta “spiders” do projeto Scrapy criado
-  Terminal: “scrapy genspider spidername site.to.scrape.com”
</details>

<details>
<summary>Instalar ipython para facilitar os testes</summary>

-  Terminal: “pip install ipython”
-  No arquivo scrapy.cfg adicionar “SHELL= ipython” em baixo de default
</details>

<details>
<summary>Usando o terminal Ipython</summary>

-  Terminal: “scrapy shell” para ativar o terminal ipython
-  No terminal Ipython (chamaremos de ITerminal):  “fetch('https://books.toscrape.com/')”
-  ITerminal: “response” ← <200 https://books.toscrape.com/>
-  Selecionando um elemento Iterminal: “response.css('article.product_pod')”
-  Sair do ITerminal usando: “exit”

- Tipos de seleção Ipython:
  -  Salvar em uma variável: “books = response.css('article.product_pod')”
  -  Verificar tamanho da lista da variável: “len(books)”
  -  Obter um item da lista: “book = books[0]”
  -  Obter o texto de um elemento “a” dentro de um elemento “h3”: “book.css('h3 a::text').get()”
  -  Obter o texto de um elemento dentro de outro elemento pela Classe: “book.css('.product_price .price_color::text').get()”
  -  Obter o conteúdo de um atributo de um elemento: “book.css('h3 a').attrib['href']” ou “response.css('.next a::attr(href)').get()”
</details>

<details>
<summary>Alterando uma Spider [nomedaspider.py](http://nomedaspider.py) (”bookspider.py”)</summary>

-  Alterar o método parse que receberá a response igual ao ITerminal [1.1](#subsecao-1-1)
</details>

<details>
<summary>Ativando e testando uma Spider pelo terminal</summary>

-  Navegar até a pasta do projeto Scrapy, nesse caso bookscraper
-  Terminal: “scrapy crawl bookspider”  Nota: o item “'item_scraped_count': 20” referencia a quantidade de itens raspados.
</details>

<details>
<summary>Percorrendo próximas páginas</summary>

-  Encontrar o elemento responsável pelo link da próxima página, nesse caso, “response.css('.next a::attr(href)').get()”
-  Adicionar lógica para percorrer próximas páginas usando callback “yield response.follow(next_page_url, callback=self.parse)” [1.2](#subsecao-1-2)
</details>
</aside>

<aside>
  
---
**Intermediário:**

<details>
<summary>Adicionando Coleta de páginas dentro da página principal</summary>

- Adicionar coleta de cada url de uma página do livro
- Adicionar método para coletar informações de uma página usando callback “yield response.follow(book_url, callback=self.parse_book_page)” [2](#subsecao-2)
</details>

<details>
<summary>Exportar os dados manualmente para um arquivo</summary>

- Terminal: “scrapy crawl bookspider -O bookdata.csv” para criar em formato csv
- Terminal: “scrapy crawl bookspider -O bookdata.json” para criar em formato json
- Terminal: “scrapy crawl bookspider -o bookdata.json” para adicionar em formato json
</details>

<details>
<summary>Criando e populando um scrapy Item</summary>

- Criar uma classe para o item no arquivo items.py [3.](#subsecao-3)
- Popular a classe do livro [3.1](#subsecao-3-1)
</details>

<details>
<summary>Rodando uma pipeline para pré-processar um item</summary>

- Habilitar a spider no arquivo de configurações da spider “settings.py” descomentando o objeto ITEM_PIPELINES = {}
  Nota: Em “ITEM_PIPELINES = {"bookscraper.pipelines.BookscraperPipeline": 300, }” o número 300 representa a prioridade, onde, quanto menor o valor mais “cedo” a pipeline vai rodar.
- Alterar o método process_item do item no arquivo “pipelines.py” [4.](#subsecao-4)
</details>

<details>
<summary>Salvando em um banco de dados</summary>

- Podemos adicionar no arquivo de configurações da spider “settings.py” um objeto FEEDS = {'booksdata.json': {'format': 'json'}} para definir um formato padrão de saída quando rodarmos o comando “scrapy crawl bookspider” que é equivalente ao comando “scrapy crawl bookspider -O cleandata.json”
- Podemos também sobrescrever uma configuração do arquivo settings.py dentro do arquivo bookspider.py (arquivo referente à spider), basta adicionar  “custom_settings = { 'FEEDS': { 'booksdata.json': {'format': 'json'}, 'overwrite': True }}” ao código
- Baixar e instalar SQLITE.
- Adicionar uma classe no arquivo pipelines.py para lidar com o banco [5.](#subsecao-5)
- Adicionar um item no objeto ITEM_PIPELINES no arquivo settings.py com: "bookscraper.pipelines.SaveToSQLitePipeline": 400,"
</details>

<details>
<summary>Evitando bloqueio de requisição de um site</summary>

- Criar método para adicionar header ao request [6.](#subsecao-6)
- Adicionar variáveis que o método necessitar [6.1](#subsecao-6-1)
- Adicionar middleware ao arquivo settings.py [6.2](#subsecao-6-2)
</details>

<details>
<summary>Adicionando proxy às requisições</summary>

- Adicionar configuração de proxy ao arquivo settings.py [7.](#subsecao-7)
- Alternativa usando um serviço pago [7.1](#subsecao-7-1)
- Alternativa usando scrapeops proxy api [7.2](#subsecao-7-2)
</details>

<details>
<summary>Rodando uma Spider na nuvem </summary> 
    
Criando um projeto Scrapy Cloud [8](#subsecao-8)

---
- Criar uma conta em “[https://app.zyte.com](https://app.zyte.com/o/599648)”
- Ir até a aba Scrapy Cloud
- Criar um novo projeto clicando em “Start Project” 
- Em Scrapy Cloud, navegar no projeto criado
- Ir na sessão “SPIDERS/Code & Deploys”
- Clicar no botão “Deploy My code”

Dando deploy do seu projeto

---
- No terminal do seu projeto instalar o “shub” com o comando “pip install shub”
- Terminal: “shub login"
- Fornecer a chave de API após “API key: SUA-CHAVE-API”
- Executar Deploy com o comando “shub deploy PROJECT-ID”
- Aguardar execução do deploy e verificar no Dashboard

Rodando o projeto

---

- No menu de navegação do site do Scrapy Cloud, ir em “JOBS/Dashboard”
- Clicar em “Run”
- Selecionar a Spider que deseja rodar
- Clicar em “Run”

*Nota: Caso não seja importado automaticamente, adicionar ao arquivo “scrapinghub.yml” a linha de código “requirements_file: requirements.txt” para que seja mapeado o arquivo de requirements.txt do projeto.* [Ver tutorial](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

</aside>


<aside>
  
---
**Mais detalhes:**
<details id="subsecao-1">
<summary>Spider base criada a partir do comando “scrapy genspyder bookspider book.toscrape.com”</summary>
   
   ```python

    import scrapy
    
    
    class BookspiderSpider(scrapy.Spider):
        name = "bookspider"
        allowed_domains = ["books.toscrape.com"]
        start_urls = ["https://books.toscrape.com"]
    
        def parse(self, response):
            pass
   ```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-1-1">
<summary>1.1 Alterando o método parse para retornar um objeto com atributos vindos da response</summary>

  ```python
    import scrapy
    
    
    class BookspiderSpider(scrapy.Spider):
        name = "bookspider"
        allowed_domains = ["books.toscrape.com"]
        start_urls = ["https://books.toscrape.com"]
    
        def parse(self, response):
            pass
  ```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-1-2">
<summary>1.2 Adicionando coleta de páginas</summary>

  ```python
  import scrapy
  
  
  class BookspiderSpider(scrapy.Spider):
      name = "bookspider"
      allowed_domains = ["books.toscrape.com"]
      start_urls = ["https://books.toscrape.com"]
  
      def parse(self, response):
          books = response.css('article.product_pod')
  
          for book in books:
              yield{
                  'name': book.css('h3 a::text').get(),
                  'price': book.css('div p.price_color::text').get(),
                  'url': book.css('h3 a').attrib['href']
              }
  
  		#------------------------------------------------------------------------------------------------
          next_page = response.css('.next a::attr(href)').get()
  
          if next_page is not None:
              if 'catalogue/' in next_page:
                  next_page_url = 'https://books.toscrape.com/' + next_page
              else:
                  next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
              yield response.follow(next_page_url, callback=self.parse)
  ```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-2">
<summary>2.Adicionando raspagem de cada página do livro</summary>

  ```python
    import scrapy
    
    
    class BookspiderSpider(scrapy.Spider):
        name = "bookspider"
        allowed_domains = ["books.toscrape.com"]
        start_urls = ["https://books.toscrape.com"]
    
        def parse(self, response):
            books = response.css('article.product_pod')
    
    #---------------------------------------Alterado-------------------------------------------------
            for book in books:
                book_relative_url = book.css('h3 a::attr(href)').get()
                if 'catalogue/' in book_relative_url:
                    book_url = 'https://books.toscrape.com/' + book_relative_url
                else:
                    book_url = 'https://books.toscrape.com/catalogue/' + book_relative_url
                yield response.follow(book_url, callback=self.parse_book_page)
    #------------------------------------------------------------------------------------------------
    
            next_page = response.css('.next a::attr(href)').get()
            if next_page is not None:
                if 'catalogue/' in next_page:
                    next_page_url = 'https://books.toscrape.com/' + next_page
                else:
                    next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
                yield response.follow(next_page_url, callback=self.parse)
    
    #----------------------------------------Adicionado----------------------------------------------
        def parse_book_page(self, response):
            table_rows = response.css("table tr")
            yield {
                'url': response.url,
                'title': response.css('.product_main h1::text').get(),
                'product_type': table_rows[1].css('td ::text').get(),
                'price_excl_tax': table_rows[2].css('td ::text').get(),
                'price_excl_tax': table_rows[2].css('td ::text').get(),
                'tax': table_rows[4].css('td ::text').get(),
                'availability': table_rows[5].css('td ::text').get(),
                'num_reviews': table_rows[6].css('td ::text').get(),
                'stars' : response.css('p.star-rating::attr(class)').get(),
                'category': response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
                'description': response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
                'price': response.css('p.price_color::text').get()
            }
    
    """
    	Nota: Em category e description foi usado Xpath
    	no caso de category foi pego o elemento irmão (de mesmo nivel) anterior ao elemento li de classe 'active'
    	no caso da description foi pego o elemento irmão (de mesmo nivel) posterior ao elemento div de cladesse 'product_description'
    """
  ```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-3">
<summary>3.Adicionando um item</summary>
  
```py
    #items.py
    
    class BookItem(scrapy.Item):
        url = scrapy.Field()
        title = scrapy.Field()
        upc = scrapy.Field()
        product_type = scrapy.Field()
        price_excl_tax = scrapy.Field()
        price_incl_tax = scrapy.Field()
        tax = scrapy.Field()
        availability = scrapy.Field()
        num_reviews = scrapy.Field()
        stars = scrapy.Field()
        category = scrapy.Field()
        description = scrapy.Field()
        price = scrapy.Field()
```
> Nota: “É possível serializar um campo ou vários campos criando uma função e passando ela como parametro serializer.”

```py
    def serialize_price(value):
        return f'£ {str(value)}'
    
    
    class BookItem(scrapy.Item):
        url = scrapy.Field()
        title = scrapy.Field()
        upc = scrapy.Field()
        product_type = scrapy.Field()
        price_excl_tax = scrapy.Field()
        price_incl_tax = scrapy.Field()
        tax = scrapy.Field()
        availability = scrapy.Field()
        num_reviews = scrapy.Field()
        stars = scrapy.Field()
        category = scrapy.Field()
        description = scrapy.Field()
        price = scrapy.Field(serializer=serialize_price)
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-3-1">
<summary>3.1 Populando a classe</summary>

```py
    #bookspider.py
    
    import scrapy
    
    from bookscraper.items import BookItem
    
    
    class BookspiderSpider(scrapy.Spider):
        name = "bookspider"
        allowed_domains = ["books.toscrape.com"]
        start_urls = ["https://books.toscrape.com"]
    
        def parse(self, response):
            books = response.css('article.product_pod')
    
            for book in books:
                book_relative_url = book.css('h3 a::attr(href)').get()
                if 'catalogue/' in book_relative_url:
                    book_url = 'https://books.toscrape.com/' + book_relative_url
                else:
                    book_url = 'https://books.toscrape.com/catalogue/' + book_relative_url
                yield response.follow(book_url, callback=self.parse_book_page)
    
            next_page = response.css('.next a::attr(href)').get()
            if next_page is not None:
                if 'catalogue/' in next_page:
                    next_page_url = 'https://books.toscrape.com/' + next_page
                else:
                    next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
                yield response.follow(next_page_url, callback=self.parse)
    
    #----------------------------Alterado---------------------------------------------
        def parse_book_page(self, response):
            table_rows = response.css("table tr")
            book_item = BookItem()
    
            book_item['url'] = response.url,
            book_item['title'] = response.css('.product_main h1::text').get(),
            book_item['upc'] = table_rows[0].css('td ::text').get(),
            book_item['product_type'] = table_rows[1].css('td ::text').get(),
            book_item['price_excl_tax'] = table_rows[2].css('td ::text').get(),
            book_item['price_incl_tax'] = table_rows[3].css('td ::text').get(),
            book_item['tax'] = table_rows[4].css('td ::text').get(),
            book_item['availability'] = table_rows[5].css('td ::text').get(),
            book_item['num_reviews'] = table_rows[6].css('td ::text').get(),
            book_item['stars'] = response.css('p.star-rating::attr(class)').get(),
            book_item['category'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
            book_item['price'] = response.css('p.price_color::text').get()
    
            yield book_item
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-4">
<summary>4 Criando uma pipeline</summary>

```py
    # Define your item pipelines here
    #
    # Don't forget to add your pipeline to the ITEM_PIPELINES setting
    # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    
    
    # useful for handling different item types with a single interface
    from itemadapter import ItemAdapter
    
    
    class BookscraperPipeline:
    
        def process_item(self, item, spider):adapter = ItemAdapter(item)
    
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
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-5">
<summary>5 Classe para lidar com o banco</summary>
    
> Nota: Os metodos open_spider,  close_spider  e  process_item serão encontrados pelo scrapy e são executados automaticamente no devido tempo de vida da spider.

```py
    #pipelines.py
    
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
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-6">
<summary>6 Criando cabeçalhos (headers)</summary>

```py
    #middlewares.py
    
    class ScrapeOpsFakeBrowserHeaderAgentMiddleware:
    
        @classmethod
        def from_crawler(cls, crawler):
            return cls(crawler.settings)
    
        def __init__(self, settings):
            self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
            self.scrapeops_endpoint = settings.get('SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT')
            self.scrapeops_fake_browser_headers_active = settings.get('SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED')
            self.scrapeops_num_results = settings.get('SCRAPEOPS_NUM_RESULTS')
            self.headers_list = []
            self._get_headers_list()
            self._scrapeops_fake_browser_headers_enabled()
    
        def _get_headers_list(self):
            payload = {'api_key': self.scrapeops_api_key}
            if self.scrapeops_num_results is not None:
                payload['num_results'] = self.scrapeops_num_results
            response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
            json_response = response.json()
            self.headers_list = json_response.get('result', [])
    
        def _get_random_browser_header(self):
            random_index = randint(0, len(self.headers_list) - 1)
            return self.headers_list[random_index]
    
        def _scrapeops_fake_browser_headers_enabled(self):
            if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_fake_browser_headers_active == False:
                self.scrapeops_fake_browser_headers_active = False
            else:
                self.scrapeops_fake_browser_headers_active = True
    
        def process_request(self, request, spider):
            random_browser_header = self._get_random_browser_header()
            request.headers['user-agent'] = random_browser_header['user-agent']
            request.headers['accept'] = random_browser_header['accept']
            request.headers['sec-ch-ua'] = random_browser_header['sec-ch-ua']
            request.headers['sec-ch-ua-mobile'] = random_browser_header['sec-ch-ua-mobile']
            request.headers['sec-ch-ua-platform'] = random_browser_header['sec-ch-ua-platform']
            request.headers['sec-fetch-site'] = random_browser_header['sec-fetch-site']
            request.headers['sec-fetch-mod'] = random_browser_header['sec-fetch-mod']
            request.headers['sec-fetch-user'] = random_browser_header['sec-fetch-user']
            request.headers['accept-encoding'] = random_browser_header['accept-encoding']
            request.headers['accept-language'] = random_browser_header['accept-language']
    
            print(random_browser_header)
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-6-1">
<summary>6.1 Adicionando variáveis</summary>

```py
    #settings.py
    
    SCRAPEOPS_API_KEY = 'a889d691-4e9a-4c25-a26b-a7faec67ebfe' #api-key-just-for-exampl;e
    
    # SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
    SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
    
    # SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
    SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
    
    SCRAPEOPS_NUM_RESULTS = 50
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-6-2">
<summary>6.2 Adicionar a classe ao middlewares</summary>

```py
    #settings.py
    
    DOWNLOADER_MIDDLEWARES = {
       # "bookscraper_project.middlewares.BookscraperDownloaderMiddleware": 543,
       # 'bookscraper.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
       'bookscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,
    }
```

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-7">
<summary>7 Configurações de proxy</summary>

> Terminal:  “pip install scrapy-rotating-proxies”

Adicionar variáveis de ambiente


```py
    #settings.py
    
    ROTATING_PROXY_LIST = [
       '45.70.204.233:4145',
       '45.7.177.224:39867',
       '187.73.55.66:5678',
    ]
    
    DOWNLOADER_MIDDLEWARES = {
       # "bookscraper_project.middlewares.BookscraperDownloaderMiddleware": 543,
       # 'bookscraper.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
       'bookscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,
       'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
       'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    }
```
<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-7-1">
<summary>7.1 Alternativa usando serviço pago smart proxy</summary>

Site: [https://dashboard.smartproxy.com](https://dashboard.smartproxy.com/login)

Tutorial: [freeCode](https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-9-rotating-proxies/)

Depois de comprar um plano seguir os passos:

> Criar um usuario

![create_user](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/7aea2b02-01da-4378-8dca-4f17c00a5206)

> Adicionar configurações

![add_configs](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/5bbdbdb5-3be3-4ecd-b7f0-b0262af0069e)

> Obter o endpoint

![get_endpoints](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/01ed0dec-f6f7-49a6-ae0e-5c497610483b)

> Criar uma classe para o proxy

![create_class_proxy](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/76f1f1e3-e789-4a7f-9bbd-0e5700ae716b)
![create_class_proxy_2](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/ca277335-814b-4585-a791-2aefacb1f64d)

> Adicionar variáveis de ambiente

![add_env_vars](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/4c808bc8-35d5-4023-bdfc-b3ef30ca8698)

>Adicionar middleware

![add_middleware](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/814f772e-e789-40d0-bf92-bcdde148ec4c)

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
</details>

<details id="subsecao-7-2">
<summary>7.2 Usando scrapeops proxy api</summary>

> Terminal: “pip install scrapeops-scrapy-proxy-sdk”

Adicionar variável de ambiente
```py
    # settings.py
    
    SCRAPEOPS_API_KEY = 'YOUR_API_KEY'
    SCRAPEOPS_PROXY_ENABLED = True
    SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}
    
    DOWNLOADER_MIDDLEWARES = {
        'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    }
```

Adicionar middleware para gerenciar as urls.

```py
    ## middlewares.py
    
    from urllib.parse import urlencode
    from scrapy import Request
    
    class ScrapeOpsProxyMiddleware:
    
        @classmethod
        def from_crawler(cls, crawler):
            return cls(crawler.settings)
    
        def __init__(self, settings):
            self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
            self.scrapeops_endpoint = 'https://proxy.scrapeops.io/v1/?'
            self.scrapeops_proxy_active = settings.get('SCRAPEOPS_PROXY_ENABLED', False)
    				self.scrapeops_proxy_settings = {}
            self._clean_proxy_settings(settings.get('SCRAPEOPS_PROXY_SETTINGS'))
    
        @staticmethod
        def _replace_response_url(response):
            real_url = response.headers.get(
                'Sops-Final-Url', def_val=response.url)
            return response.replace(
                url=real_url.decode(response.headers.encoding))
        
        def _clean_proxy_settings(self, proxy_settings):
            if proxy_settings is not None:
                for key, value in proxy_settings.items():
                    clean_key = key.replace('sops_', '')
                    self.scrapeops_proxy_settings[clean_key] = value
        
        def _get_scrapeops_url(self, request):
            payload = {'api_key': self.scrapeops_api_key, 'url': request.url}
            
            ## Global Request Settings
            if self.scrapeops_proxy_settings is not None:
                for key, value in self.scrapeops_proxy_settings.items():
                    payload[key] = value
    
            ## Request Level Settings 
            for key, value in request.meta.items():
                if 'sops_' in key:
                    clean_key = key.replace('sops_', '')
                    payload[clean_key] = value
    
            proxy_url = self.scrapeops_endpoint + urlencode(payload)
            return proxy_url
    
        def _scrapeops_proxy_enabled(self):
            if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_proxy_active == False:
                return False
            return True
        
        def process_request(self, request, spider):
            if self._scrapeops_proxy_enabled is False or self.scrapeops_endpoint in request.url:
                return None
            
            scrapeops_url = self._get_scrapeops_url(request)
            new_request = request.replace(
                cls=Request, url=scrapeops_url, meta=request.meta)
            return new_request
    
        def process_response(self, request, response, spider):
            new_response = self._replace_response_url(response)
            return new_response
```

Resultado:
![result](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/e8121f43-6645-4184-a77f-5e60505cbc78)

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>   
</details>

<details id="subsecao-8">
<summary>8 Rodando projeto na nuvem usando Scrapy Cloud</summary>

>Criar uma conta em “https://app.zyte.com/account/login/?next=/o/599648/scrapycloud/discover”

![1](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/f14d3352-e74f-44ec-8a8b-2214677a287b)

>no menu lateral navegar até scrapy Cloud

![2](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/9478d467-0763-4379-a149-27742b2f1762)

>Clicar em start project

![3](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/d34eaf9a-71b9-4f7c-8dcb-0b9283ccfe11)

>Dar um nome ao projeto

![6](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/c382ebc5-e95b-4fda-8f77-b7146a582a1a)

>Navegar a pagina de Code & Deploy 1.0

![7](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/0f8e21b3-3d58-48de-9c40-4d57b185a9cd)

>Navegar a pagina de Code & Deploy 1.1

![8](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/fb7c767f-9f90-4c3d-91aa-32db42826555)

>Instalar shub no projeto (O projeto atual foi criado no Pycharm  então foi usado o próprio console do Pycharm)

![9](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/25680d88-d3b6-4605-89b1-5cd735aee312)

>Logar no shub 1.0: digitar comando de login

![10](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/c84f7e7c-e005-430d-b8e6-43beed645f2e)

>Logar no shub 1.1: Inserir chave API 

![11](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/ba94fcc6-bcc0-4228-824d-de03c03f51e4)

![11 1](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/5b144044-988d-488f-8ce7-d7d2bca436de)
>Executar Deploy do projeto para o shub

![12](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/34e4c303-5417-45ef-9d11-033bfeb55b56)

>Aguardar o Deplyoy

![13](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/5dc44f12-d4c8-4267-a09f-0977d543cb41)

>Sucesso!

![14](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/cbd4e79b-aaaf-4d1b-8aac-b0fac2ddbf16)

>Inserir o nome da Spider e Clicar em Run

![15](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/098243d2-58c8-4323-86ca-f819ff853570)

>Navegar até o Dashboard do projeto e clicar em Run

![16](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/16a897ba-3124-4e45-a9db-d046f3f7ee99)

>Virificar conclusão na seção “Completed”

![17](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/5eb27a5c-c670-4daa-8396-48a228990970)

>Acompanhar execução na seção “Running”

![18](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/0433c7a6-77cb-4240-9b99-4e938e36344c)

>No caso atual ocorreram 4 erros, para investigar melhor clicaremos no numero logo abaixo da coluna “Errors”na tabela da seção “Completed”.

![19](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/bdda0a79-8ee7-4395-a936-ebab225b7fed)

>Podemos investigar os erros na seguinte página, podendo expandir cada erro para ver o log do erro em específico. 

![20](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/27b63610-61b0-479f-813d-34a5b4fd25ca)

>O erro é decorrido da falta do módulo “itemadapter” que utilizamos em uma classe dentro do arquivo pupelines.py para indicar um livro como um item

![21](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/86bd34fb-16b4-4db0-9bcd-7379381b4e35)

>O erro em questão está ocorrendo pois no deploy do projeto não estamos indicando os requisitos que o projeto está utilizando. 
para isso criaremos um arquivo requirements.txt na raiz do nosso projeto e adicionaremos a versão do itemadapter que estamos utilizando

![22](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/483d0c3a-37dd-46c2-a473-2dc2910eeb95)

>Em seguida no arquivo scrapinghub.yml adicionaremos a linha de código “requirements_file: requirements.txt” logo a baixo do id 
do projeto para indicar o caminho do nosso arquivo requirements.

![23](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/24e31841-4d24-40f3-9c15-3bcad6007d66)

>Executaremos novamente o Deploy do projeto

![24](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/07665c05-e8c2-4590-a629-582404c3c0e5)

>No site de gerenciamento de deploy iremos navegar até a seção de deploy para verificar o andamento do nosso deploy

![25](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/1b72b23c-7a50-452d-bb9e-cc4593dd2180)

>Aguardaremos o progesso do deploy. Note que temos um numero 2 que indica que esse é o segundo deploy desse projeto.

![26](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/b0070adf-edfc-4adb-a19e-f72bd6276be5)

>Indicação de sucesso do deploy.

![27](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/cc63eeeb-722e-4211-a373-dcde04cb6197)

>Podemos clicar na seção que acabamos de  implantar(Deploy) e navegar até a aba “Requirements” para 
verificar que nosso requirements.txt foi implementado com sucesso! 

![28](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/1ed4dd57-b921-4e67-95aa-63293c520394)

>Seguiremos os passos de execução da spider e se tudo correr bem teremos uma execução em andamento da
nossa spyder. caso contrario investigue os erros para resolver o problema.

![29](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/a3464210-1c88-4e56-b367-22e4a941e4f7)

>Agora no Dashboard podemos ver que a spyder rodou com sucesso e tambem podemos ver a que falhou.

![30](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/55232194-f55c-4ae6-b8e1-e9e0b3a67739)

>Clicando no numero do item podemos verificar os itens coletados.

![31](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/3d15d95c-5dcc-491f-a8e4-75fc2fcd6a7d)

>Nessa parte também é possível baixar todos os itens em um formato desejado dentre os disponiveis.

![32](https://github.com/Lucas382/ScrapyTemplate/assets/44009909/7f2d948a-2dea-4f75-801d-2071c0388231)


<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p> 
</details>
<aside>
