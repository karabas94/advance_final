# Bookshop

## Function of shop
* Celery(periodically synch books from store to shop, orders from shop to store(used API) and back)
* Search books
* Filtration by genre
* Pagination 
* Review of book
* Tracking order
* Annotation
* Cart(used session)
* Login/Registration
* Feedback
* Mailhog receive email message

## How to start project
1. Create shop.env, store.env and complete environment
```
DJANGO_SECRET_KEY=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
API_STORE_KEY= --only for shop.env--
```
2. Download docker and docker-compose

3. Start docker compose and project
    ```bash
       docker-compose build
      ```
    ```bash
       docker-compose up
      ```
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