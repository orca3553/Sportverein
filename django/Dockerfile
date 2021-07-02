FROM python:3.9

RUN apt install default-libmysqlclient-dev
RUN pip install --no-cache \
    mysqlclient \
    Django

USER 1000:1000

WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
