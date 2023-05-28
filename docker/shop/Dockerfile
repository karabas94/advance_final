FROM python:3.10

COPY shop/requirements.txt app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY shop/ /app

WORKDIR /app

EXPOSE 8000

CMD ["sh", "runserver.sh"]