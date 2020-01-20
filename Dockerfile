#FROM python:3.7-alpine
#MAINTAINER Luch developer
#
#ENV PYTHONUNBUFFERED 1
#
#COPY ./requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt
#
#
#
#RUN mkdir /app
#WORKDIR /app
#
#COPY ./app /app
#
##RUN adduser -D user
##USER user

FROM python:3
RUN mkdir src/
COPY requirements src/
WORKDIR /src/
RUN pip install -r requirements
ADD . /src/