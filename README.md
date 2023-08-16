<aside>
👣 *Passo a passo:*

---

**Instalação e primeiro contato:**

- Instalação Scrapy
    - [ ]  Criar um novo projeto com ambiente virtual
    - [ ]  Abrir terminal e instalar o Scrapy com o comando “pip install Scrapy”
- Criar um projeto de Spider
    - [ ]  Terminal: “scrapy startproject nomedoprojetoscraper”
- Criar uma Spider
    - [ ]  Navegar até a pasta “spiders” do projeto Scrapy criado
    - [ ]  Terminal: “scrapy genspider spidername site.to.scrape.com”
- Instalar ipython para facilitar os testes
    - [ ]  Terminal: “pip install ipython”
    - [ ]  No arquivo scrapy.cfg adicionar “SHELL= ipython” em baixo de default
- Usando o terminal Ipython
    - [ ]  Terminal: “scrapy shell” para ativar o terminal ipython
    - [ ]  No terminal Ipython(chamaremos de: ITerminal):  “fetch('https://books.toscrape.com/')”
    - [ ]  ITerminal: “response” ← <200 https://books.toscrape.com/>
    - [ ]  Selecionando um elemento Iterminal: “response.css('article.product_pod')”
    - [ ]  Sair do ITerminal usando: “exit”
    - Tipos de seleção Ipython
        
        Salvar em uma variavel: “books = response.css('article.product_pod')”
        
        Verificar tamanho da lista da variável: “len(books)”
        
        Obter um item da lista: “book = books[0]”
        
        Obter o texto de um elemento “a” dentro de um elemento “h3”: “book.css('h3 a::text').get()”
        
        Obter o texto de um elemento dentro de outro elemento pela Classe: “book.css('.product_price .price_color::text').get()”
        
        Obter o conteúdo de um atributo de um elemento: “book.css('h3 a').attrib['href']” ou “response.css('.next a::attr(href)').get()”
        
- Alterando uma Spider [nomedaspider.py](http://nomedaspider.py) (”bookspider.py”)
    - [ ]  Alterar o método parse que receberá a response igual ao ITerminal [1.1](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
- Ativando e testando uma Spider pelo terminal
    - [ ]  Navegar até a pasta do projeto Scrapy, nesse caso bookscraper
    - [ ]  Terminal: “scrapy crawl bookspider”  Nota: o item “'item_scraped_count': 20” referencia a quantidade de itens raspados.
- Percorrendo próximas páginas
    - [ ]  Encontrar o elemento responsável pelo link da proxima página, nesse caso, “*response*.css('.next a::attr(href)').get()”
    - [ ]  Adicionar lógica para percorrer próximas páginas  usando callback “yield response.follow(next_page_url, callback=self.parse)” [1.2](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</aside>
