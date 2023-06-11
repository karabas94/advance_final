# Bookshop

## Function of shop
* Celery
  * synchronization book from store to shop
  * synchronization order from shop to store(sent to API)
  * synchronization order status from store to shop
* Search books
* Filtration by genre
* Pagination 
* Review of book
* Tracking order
* DB queries optimized
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
   https://docs.docker.com/engine/install/
3. Start docker compose and project
    ```bash
       docker-compose build
      ```
    ```bash
       docker-compose up
      ```
4. Create API_STORE_KEY in store admin panel and don't forget complete environment file

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