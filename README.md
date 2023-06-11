# Bookshop
This bookshop project is developed on Django, and it has two backends with different PostgreSQL databases. 
The store is developed using the Django REST framework API.

## Developed in the project:
* Celery
  * synchronization book from store to shop
  * synchronization order from shop to store(sent to API)
  * synchronization order status from store to shop
* Book search
* Genre filtering
* Pagination
* Book reviews
* Order tracking 
* Database optimization
* Shopping cart (uses session, the user can't add more items than available quantity)
* Registration and login
* Feedback form
* Page caching for book pages
* Mailhog receive email message

## How to start project
1. Clone this repository.
2. Create shop.env, store.env and complete environment
```
DJANGO_SECRET_KEY=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
API_STORE_KEY= --only for shop.env--
```
3. Download docker and docker-compose
   https://docs.docker.com/engine/install/
4. Start docker compose and project
    ```bash
    docker-compose build
      ```
    ```bash
    docker-compose up
      ```
   or
    ```bash
    docker compose build
      ```
    ```bash
    docker compose up
      ```
5. Create API_STORE_KEY in store admin panel and don't forget complete environment file.
You may need to restart Celery for proper functioning after adding a API key.

## Links
* Shop
```
http://localhost/
```
* Store
```
http://localhost:8001/
```
* Mailhog
```
http://localhost:8025/
```