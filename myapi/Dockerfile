# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
    
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . .
EXPOSE 8000

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]