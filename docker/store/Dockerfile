FROM python:3.10

COPY store/requirements.txt app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY wait-for-command.sh /

COPY store/docker-entrypoint.sh /

COPY store/ /app

WORKDIR /app

EXPOSE 8000

RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh runserver.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["sh", "runserver.sh"]