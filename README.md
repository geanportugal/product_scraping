# Backend Challenge 20220626

## Introdução

O projeto tem como objetivo dar suporte a equipe de nutricionistas da empresa Fitness Foods LC para que possam comparar de maneira rápida a informação nutricional dos alimentos da base do Open Food Facts.

## Técnologias utilizadas

- Python 
- Django 
- Django Rest Framework
- Celery
- RabbitMQ
- Redis Cache
- MongoDB
- Docker

### Instalando o Projeto:
- Faça o clone do projeto em sua máquina local - git clone
- Instale o Docker Desktop [here](https://www.docker.com/get-started)
### Configurando o Projeto:
- Configure as variáveis de ambiente
    * Renomei o arquivo .env_example para .env
    * gere uma nova secret_key - Execute o comando o no console python
    * insira a nova secret no arquivo .env
    ```python
       import secrets
       print(secrets.token_urlsafe()
    ```
    * Configure os arquivos de smtp para o envio de notifições
    ```python
        EMAIL_HOST = 'smtp.example.com'
        EMAIL_PORT = 587
        EMAIL_HOST_USER = 'username@example.com'
        EMAIL_HOST_PASSWORD = 'password'
        EMAIL_USE_TLS = True
    ```
    * Para as demais variáveis não são necessárias nenhuma ação 
    
### Rodando a aplicação em um docker container
    - docker-compose up --build
    - acesse [127.0.0.1:8000](http://127.0.0.1:8000) 


## Acessando os endpoints da API
 - `/products` lista todos os produtos  
 - `/products/<code>` mostra um produto
 - `/docs/` Mostra a documentação
 - `/schema/` Mostra os schemas


>  This is a challenge by [Coodesh](https://coodesh.com/)
