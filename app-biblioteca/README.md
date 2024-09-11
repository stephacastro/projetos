# app-biblioteca

## Documentação do projeto
####  Este projeto é um aplicativo Python em FastApi com todo ambiente de execução encapsulado em Docker.
#### Objeto desse aplicativo é criar um gerenênciador de livros para bibliotecas.

# Dependências

## Criação de ambiente virtual
    python3 -m venv env

## Ativação do ambiente virtual
    source env/bin/activate

## Instalação das bibliotecas para testar o aplicativo local
    pip install -r requirements.txt

## Instalou bibliotecas nova no projeto?? Não esqueça de atualizar o requiretems
    pip freeze > requirements.txt

## O projeto esta todo encapsulado em Docker, para construir a imagem e o container do aplicativo e do banco...
    docker compose up

## Documentação FastApi, com endpoints e etc...
    http://localhost:8000/docs

## Finalizou o projeto?... Não deixe o docker consumindo os recursos da sua máquina
    docker compose down

## Alguns comandos Dockers que em algum momento podem precisar ser utilizados...
    docker volume rm mysql_database   >>> Deleta um container especifico
    docker volume prune   >>> Deleta todos os containers existentes
    docker rmi <IMAGE_ID ou NAME>   >>> Deleta uma imagem
    docker-compose up --build   >>> Reconstrói e reinicia os serviços
