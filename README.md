
# Board game shop API

This is CRUD REST API for board game shop written in Python3 using Django and DRF.


## Stack
- Python3
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djoser](https://djoser.readthedocs.io/en/latest/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Docker](https://www.docker.com/)


## Features
 - User create/login/signup/restore
 - Create/list/retrieve/update/delete for
     - game
     - game category
     - author
     - order
 - Permissions: 
     - regular users can't add or edit game, game category and author
     - user has access only for his own orders 
 - Ordering games by cost, playing time, released year
 - Filtering games by game category and author
 - Search games by name
 - Pagination
 - Authentication provided by JWT
 - Docker support


## Usage
Action | URL | Method
------------ | ------------- | -------------
Create user | /api/v1/auth/users/ | POST
Obtain token | /api/v1/auth/token/ | POST
Refresh token | /api/v1/auth/refresh/ | POST
Create/List game | /api/v1/games/ | POST/GET 
Get/Update/Delete game | /api/v1/games/<int:pk> | GET/UPDATE/DELETE 
Create/List game category | /api/v1/game_category/ | POST/GET 
Get/Update/Delete game category | /api/v1/game_category/<int:pk> | GET/UPDATE/DELETE 
Create/List author | /api/v1/authors/ | POST/GET 
Get/Update/Delete author | /api/v1/authors/<int:pk> | GET/UPDATE/DELETE 
Create/List order | /api/v1/orders/ | POST/GET 
Get/Update/Delete order | /api/v1/orders/<int:pk> | GET/UPDATE/DELETE 

## Setup
Clone the repository and change the working directory:

    git clone https://github.com/vanyabondar/boardgame_backend
    cd boardgame_backend
Create .env file with your environment variables:

    SECRET_KEY=***** 
    DB_NAME=*****
    DB_USER=*****
    DB_PASSWORD=*****
    DB_HOST=*****
    DB_PORT=*****
### Run from docker image 
Build image from Dockerfile:
    
    sudo docker build -t boardgame_backend .
Run container

    sudo docker run -p 8000:8000 boardgame_backend


### Run by python

Create and activate the virtual environment:

    python3 -m venv ./venv
    source ./venv/bin/activate
Install requirements:

    pip3 install -r requirements.txt


Run the server:

    python3 manage.py runserver
   
