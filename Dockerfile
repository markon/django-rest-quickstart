FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/v.3.6/main --no-cache postgresql-dev
RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/v.3.6/main --no-cache gcc
RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/v.3.6/main --no-cache python3-dev
RUN apk add --repository http://dl-cdn.alpinelinux.org/alpine/v.3.6/main --no-cache musl-dev

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip3 install pipenv
RUN pipenv --three
RUN pipenv install --deploy --system

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
