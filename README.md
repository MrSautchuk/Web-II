# 💻 Web II - Práticas e Exercícios

Repositório destinado aos códigos, exercícios e anotações desenvolvidos durante as aulas da disciplina de Desenvolvimento Web II. 

O foco deste repositório é o aprendizado prático e a evolução na programação web, iniciando com a lógica e sintaxe pura da linguagem Python, e avançando para o desenvolvimento de APIs e rotas web utilizando o microframework Flask.

## 🚀 Tecnologias

Atualmente, o repositório foca nos fundamentos em:
* **Python** (Puro)
* **Flask** (Microframework)
* *[Outras tecnologias serão adicionadas conforme o avanço das aulas]*

## 📂 Estrutura do Repositório

Os arquivos estão organizados para facilitar a consulta rápida. 

* `Aulas_python/` - Códigos de lógica base.
  * `./01) Estrutura Sequencial (IO)`
  * `./02) Estrutura de Decisão`
  * `./03) Estrutura de Repetição`
  * `./Atividades em Sala`
  * `./Slides`
* `Projeto Flask/` - Resolução de exercícios práticos de rotas HTTP, parâmetros dinâmicos e templates Jinja2.

## 🏃 Como executar os projetos

### Scripts em Python Puro (`Aulas_python`)
A execução é simples e direta, necessitando apenas do [Python instalado](https://www.python.org/downloads/).

1. Clone e acesse o repositório:
   ```bash
   git clone [https://github.com/MrSautchuk/Web-II.git](https://github.com/MrSautchuk/Web-II.git)
   cd Web-II

2. Navegue até a pasta desejada e execute:
   ```bash
   python nome_do_arquivo.py
   
Aplicação Web (Projeto Flask)
Por utilizar um framework, é necessário rodar o projeto de forma isolada usando um ambiente virtual.

1. Acesse o diretório do projeto:
   ```bash
   cd "Projeto Flask"

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate

3. Instale a dependência e inicie o servidor:
   ```bash
   pip install flask
   python app.py

[!NOTE]
Dependendo da configuração do seu sistema operacional, pode ser necessário utilizar o comando python3. Para ativar o ambiente virtual em terminais Linux/Mac, o comando é source .venv/bin/activate.
