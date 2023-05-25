FROM python:3.10

COPY store/requirements.txt app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY store/ /app

WORKDIR /app

EXPOSE 8000

CMD ["sh", "runserver.sh"]