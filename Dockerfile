# pythonのバージョンは任意
FROM python:3.8

WORKDIR /app
ENV FLASK_APP=app
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update