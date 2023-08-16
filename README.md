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

-  Alterar o método parse que receberá a response igual ao ITerminal [Seção 1](#Seção-1)
</details>

<details>
<summary>Ativando e testando uma Spider pelo terminal</summary>

-  Navegar até a pasta do projeto Scrapy, nesse caso bookscraper
-  Terminal: “scrapy crawl bookspider”  Nota: o item “'item_scraped_count': 20” referencia a quantidade de itens raspados.
</details>

<details>
<summary>Percorrendo próximas páginas</summary>

-  Encontrar o elemento responsável pelo link da próxima página, nesse caso, “response.css('.next a::attr(href)').get()”
-  Adicionar lógica para percorrer próximas páginas usando callback “yield response.follow(next_page_url, callback=self.parse)” [1.2](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>
</aside>

<aside>
  
---
**Intermediário:**

<details>
<summary>Adicionando Coleta de páginas dentro da página principal</summary>

- Adicionar coleta de cada url de uma página do livro
- Adicionar método para coletar informações de uma página usando callback “yield response.follow(book_url, callback=self.parse_book_page)” [2.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

<details>
<summary>Exportar os dados manualmente para um arquivo</summary>

- Terminal: “scrapy crawl bookspider -O bookdata.csv” para criar em formato csv
- Terminal: “scrapy crawl bookspider -O bookdata.json” para criar em formato json
- Terminal: “scrapy crawl bookspider -o bookdata.json” para adicionar em formato json
</details>

<details>
<summary>Criando e populando um scrapy Item</summary>

- Criar uma classe para o item no arquivo items.py [3.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Popular a classe do livro [3.1](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

<details>
<summary>Rodando uma pipeline para pré-processar um item</summary>

- Habilitar a spider no arquivo de configurações da spider “settings.py” descomentando o objeto ITEM_PIPELINES = {}
  Nota: Em “ITEM_PIPELINES = {"bookscraper.pipelines.BookscraperPipeline": 300, }” o número 300 representa a prioridade, onde, quanto menor o valor mais “cedo” a pipeline vai rodar.
- Alterar o método process_item do item no arquivo “pipelines.py” [4.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

<details>
<summary>Salvando em um banco de dados</summary>

- Podemos adicionar no arquivo de configurações da spider “settings.py” um objeto FEEDS = {'booksdata.json': {'format': 'json'}} para definir um formato padrão de saída quando rodarmos o comando “scrapy crawl bookspider” que é equivalente ao comando “scrapy crawl bookspider -O cleandata.json”
- Podemos também sobrescrever uma configuração do arquivo settings.py dentro do arquivo bookspider.py (arquivo referente à spider), basta adicionar  “custom_settings = { 'FEEDS': { 'booksdata.json': {'format': 'json'}, 'overwrite': True }}” ao código
- Baixar e instalar SQLITE.
- Adicionar uma classe no arquivo pipelines.py para lidar com o banco [5.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Adicionar um item no objeto ITEM_PIPELINES no arquivo settings.py com: "bookscraper.pipelines.SaveToSQLitePipeline": 400,"
</details>

<details>
<summary>Evitando bloqueio de requisição de um site</summary>

- Criar método para adicionar header ao request [6.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Adicionar variáveis que o método necessitar [6.1](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Adicionar middleware ao arquivo settings.py [6.2](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

<details>
<summary>Adicionando proxy às requisições</summary>

- Adicionar configuração de proxy ao arquivo settings.py [7.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Alternativa usando um serviço pago [7.1](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Alternativa usando scrapeops proxy api [7.2](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

<details>
<summary>Rodando uma Spider na nuvem </summary>[8.](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)

Criando um projeto Scrapy Cloud

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
<details>
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
</details>

## Seção 1
<details>
   <summary>  Alterando o método parse para retornar um objeto com atributos vindos da response</summary>
   ```python
    import scrapy


    class BookspiderSpider(scrapy.Spider):
        name = "bookspider"
        allowed_domains = ["books.toscrape.com"]
        start_urls = ["https://books.toscrape.com"]
    
        def parse(self, response):
            books = response.css('article.product_pod')
    
    #------------------------------------------------------------------------------------------------
            for book in books:
                yield{
                    'name': book.css('h3 a::text').get(),
                    'price': book.css('div p.price_color::text').get(),
                    'url': book.css('h3 a').attrib['href']
    
                }
   ```
</details>

<aside>
