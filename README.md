# Backend Challenge 20220626



- Deve conter o título do projeto
- Uma descrição sobre o projeto em frase
- Deve conter uma lista com linguagem, framework e/ou tecnologias usadas
- Como instalar e usar o projeto (instruções)
- Não esqueça o [.gitignore](https://www.toptal.com/developers/gitignore)
- Se está usando github pessoal, referencie que é um challenge by coodesh:  

>  This is a challenge by [Coodesh](https://coodesh.com/)


## Introdução

O projeto tem como objetivo dar suporte a equipe de nutricionistas da empresa Fitness Foods LC para que possam comparar de maneira rápida a informação nutricional dos alimentos da base do Open Food Facts.

## O projeto

- Python 
- Django 
- Django Rest Framework
- Celery
- RabbitMQ
- Redis Cache
- MongoDB
- Docker

### Instalando o Projeto:
- Para instalar o projeto é necessário fazer o clone do projeto em sua máquina local e executar o arquivo docker-compose com o docker instalado e executando
- Para o envio de email de notificação de erros abra o arquivo settings.py e insira seu e-mail na constante EMAIL_ADMIN
    é necessário configurar o servidor smtp
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'username@example.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_USE_TLS = True



>  This is a challenge by [Coodesh](https://coodesh.com/)