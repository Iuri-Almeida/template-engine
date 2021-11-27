<div align='center'>
  
  <img width="280" src="https://user-images.githubusercontent.com/60857927/143660431-4c75fe0c-5287-435a-a1f8-357cd5c67ef3.png" />
  
</div>

<div align = "center">

<p>

  <a href="#descricao">Descrição</a> &#xa0; | &#xa0;
  <a href="#tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#requisitos">Requisitos</a> &#xa0; | &#xa0;
  <a href="#executando">Executando</a> &#xa0; | &#xa0;
  <a href="#como_funciona">Como funciona?</a> &#xa0; | &#xa0;
  <a href="#referencias">Referências</a>

</p>

</div>

<div id = "descricao">

## :pushpin: Descrição ##

<p>

  Esse é o repositório da minha versão de uma **Template Engine**, uma ferramenta bastante utilizada para o desenvolvimento de aplicações web. A ideia inicial desse projeto era criar uma Template Engine do zero e entender como funciona essa ferramenta por trás dos panos.

</p>

</div>

<div id = "tecnologias">

## :rocket: Tecnologias ##

Todas as tecnologias usadas na realização do projeto:

* [Python][python] [Versão 3.8]
* [PyCharm][pycharm]

</div>

<div id = "requisitos">

## :warning: Requisitos ##

<p>

  Antes de executar, você precisar ter o [Git][git] e o [Python][python] (Versão 3.8) instalados na sua máquina.

</p>

</div>

<div id = "executando">

## :computer: Executando ##

<p>

  Depois de correr tudo certo na instalação, está na hora de clonar o repositório.

</p>

```bash
# Clone este projeto
$ git clone https://github.com/Iuri-Almeida/template-engine.git
# Acesse a pasta do projeto
$ cd template-engine
```

</div>

<div id = "como_funciona">

## :eyes: Como funciona? ##

<p>

  Como essa é uma Template Engine bem simples, temos apenas as funcionalidades de `comentários`, `variáveis`, estruturas `if`, `for` e `def` e acesso à `dicionários` (objetos), com suas devidas **limitações**. Segue alguns exemplos da utilização dessas estruturas.

</p>

* `comentários`

  ```python
  from template_engine import TemplateEngine
  
  template = '''
  {# Isso é um comentário #}
  <p>Hello, world!</p>
  '''
  engine = TemplateEngine(template)
  html = engine.render()
  ```
  ```html
  <p>Hello, world!</p>
  ```

* `variáveis`

  ```python
  from template_engine import TemplateEngine
  
  template = '<p>Hello, {{ name }}!</p>'
  engine = TemplateEngine(template)
  html = engine.render({'name': 'Iuri'})
  ```
  ```html
  <p>Hello, Iuri!</p>
  ```

* `if` <br />

  ```python
  from template_engine import TemplateEngine
  
  template = '''
  {% if CONDICAO %}
      <p>Hello, {{ name }}!</p>
  {% endif %}
  '''
  engine = TemplateEngine(template)
  html = engine.render({'name': 'Iuri', 'CONDICAO': True})
  ```
  ```html
  <!-- Funcionando apenas se CONDIÇÃO for do tipo `bool` -->
  <p>Hello, Iuri!</p>
  ```

* `for` <br />

  ```python
  from template_engine import TemplateEngine
  
  template = '''
  <ul>
      {% for i in LISTA %}
          <li>{{ i }}</li>
      {% endfor %}
  </ul>
  '''
  engine = TemplateEngine(template)
  html = engine.render({'LISTA': ['PC', 'PlayStation', 'XBox']})
  ```
  ```html
  <ul>
      <li>PC</li>
      <li>PlayStation</li>
      <li>XBox</li>
  </ul>
  ```

* `def` <br />

  ```python
  from template_engine import TemplateEngine
  
  def format_price(price: float) -> str:
      return f'{price:.2f}'
  
  template = '<span>Preço: R$ {{ PRECO::FORMATACAO }}!</span>'
  engine = TemplateEngine(template)
  html = engine.render({'PRECO': 999, 'FORMATACAO': format_price})
  ```
  ```html
  <span>Preço: R$ 999.00!</span>
  ```

* `dicionários` (objetos) <br />

  ```python
  from template_engine import TemplateEngine
  
  template = '<span>O usuário {{ USUARIO.nome }} tem {{ USUARIO.idade }} anos!</span>'
  engine = TemplateEngine(template)
  html = engine.render({'USUARIO': {'nome': 'Iuri', 'idade': 22}})
  ```
  ```html
  <span>O usuário Iuri tem 22 anos!</span>
  ```

</div>

<div id = "referencias">

## :key: Referências ##

Alguns locais de onde me baseei para realizar o projeto:

* [Artigo - Template Engine][article]

:mag: &#xa0; Os ícones usados nesse README foram tirados desse [repositório][icones].

</div>

<!-- Links -->
[article]: https://www.aosabook.org/en/500L/a-template-engine.html
[python]: https://www.python.org/
[pycharm]: https://www.jetbrains.com/pycharm/
[git]: https://git-scm.com
[icones]: https://gist.github.com/rxaviers/7360908