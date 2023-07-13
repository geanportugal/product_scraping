# Backend Challenge 20220626

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
- Para instalar o projeto é necessário fazer o clone do projeto em sua máquina local 
- Crie uma virtualenv 
- Instale os requirements
    * Você pode também tentar executar o arquivo active_workspace.py
        - python active_workspace.py
### Configurando o Projeto:
- Para o envio de email de notificação de erros abra o arquivo settings.py e insira seu e-mail na constante EMAIL_ADMIN
    é necessário configurar o servidor smtp
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'username@example.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_USE_TLS = True
    
### Executando o projeto:
    - python manage.py runserver
    - celery -A core worker -l info
    - celery -A core beat -l info


>  This is a challenge by [Coodesh](https://coodesh.com/)