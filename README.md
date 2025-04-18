Blog_Flask

Meu primeiro projeto web com Flask

Este projeto é uma aplicação web simples de blog, desenvolvida com Python e o framework Flask, que permite ao usuário criar, visualizar, editar e excluir postagens. Os dados são armazenados em um banco de dados SQLite, utilizando o ORM SQLAlchemy para facilitar a manipulação dos dados.
Funcionalidades:

Mostrar postagens: Lista todos os posts cadastrados.

Adicionar postagem: Permite criar um novo post com título, autor e conteúdo.

Editar postagem: Atualiza os dados de uma postagem existente.

Excluir postagem: Remove uma postagem do sistema pelo ID.

Visualização de posts: Apresenta os dados de forma simples em uma página HTML.

Tratamento dos dados:

As postagens são armazenadas no banco blog.sqlite3.

O banco é criado automaticamente ao iniciar o programa, caso não exista.

Toda a manipulação de dados (inserção, exclusão, atualização e listagem) é feita através do SQLAlchemy.

Organização:

app.py: Arquivo principal, responsável por iniciar o app Flask e o banco de dados.

models.py: Define a estrutura da tabela Post.

routes.py: Contém todas as rotas e regras de funcionamento da aplicação.

templates/: Pasta onde ficam os arquivos HTML (index.html e edit.html).

Requisitos:

Python 

Flask

Flask-SQLAlchemy
