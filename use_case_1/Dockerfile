FROM python:3.9.16

RUN apt-get update
RUN apt-get -y upgrade

COPY ./requirements.txt /message/requirements.txt
WORKDIR /message

RUN python3.9 -m pip install -r requirements.txt

COPY ./message /message

EXPOSE 6401

ENV PYTHONPATH="/message"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
