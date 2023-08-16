<aside>
👣 *Passo a passo:*

---

**Instalação e primeiro contato:**

<details>
<summary>Instalação Scrapy</summary>

- [ ] Criar um novo projeto com ambiente virtual
- [ ] Abrir terminal e instalar o Scrapy com o comando “pip install Scrapy”
</details>

<details>
<summary>Criar um projeto de Spider</summary>

- [ ] Terminal: “scrapy startproject nomedoprojetoscraper”
</details>

<details>
<summary>Criar uma Spider</summary>

- [ ] Navegar até a pasta “spiders” do projeto Scrapy criado
- [ ] Terminal: “scrapy genspider spidername site.to.scrape.com”
</details>

<details>
<summary>Instalar ipython para facilitar os testes</summary>

- [ ] Terminal: “pip install ipython”
- [ ] No arquivo scrapy.cfg adicionar “SHELL= ipython” em baixo de default
</details>

<details>
<summary>Usando o terminal Ipython</summary>

- [ ] Terminal: “scrapy shell” para ativar o terminal ipython
- [ ] No terminal Ipython (chamaremos de ITerminal):  “fetch('https://books.toscrape.com/')”
- [ ] ITerminal: “response” ← <200 https://books.toscrape.com/>
- [ ] Selecionando um elemento Iterminal: “response.css('article.product_pod')”
- [ ] Sair do ITerminal usando: “exit”

- Tipos de seleção Ipython:
  - [ ] Salvar em uma variável: “books = response.css('article.product_pod')”
  - [ ] Verificar tamanho da lista da variável: “len(books)”
  - [ ] Obter um item da lista: “book = books[0]”
  - [ ] Obter o texto de um elemento “a” dentro de um elemento “h3”: “book.css('h3 a::text').get()”
  - [ ] Obter o texto de um elemento dentro de outro elemento pela Classe: “book.css('.product_price .price_color::text').get()”
  - [ ] Obter o conteúdo de um atributo de um elemento: “book.css('h3 a').attrib['href']” ou “response.css('.next a::attr(href)').get()”
</details>

<details>
<summary>Alterando uma Spider [nomedaspider.py](http://nomedaspider.py) (”bookspider.py”)</summary>

- [ ] Alterar o método parse que receberá a response igual ao ITerminal [1.1](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>

<details>
<summary>Ativando e testando uma Spider pelo terminal</summary>

- [ ] Navegar até a pasta do projeto Scrapy, nesse caso bookscraper
- [ ] Terminal: “scrapy crawl bookspider”  Nota: o item “'item_scraped_count': 20” referencia a quantidade de itens raspados.
</details>

<details>
<summary>Percorrendo próximas páginas</summary>

- [ ] Encontrar o elemento responsável pelo link da próxima página, nesse caso, “response.css('.next a::attr(href)').get()”
- [ ] Adicionar lógica para percorrer próximas páginas usando callback “yield response.follow(next_page_url, callback=self.parse)” [1.2](https://www.notion.so/Page-3-Scrapy-Project-4aa86e19a54c459c9b5d4465e564ea92?pvs=21)
</details>
</aside>
