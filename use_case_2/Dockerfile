FROM python:3.9.16

RUN apt-get update
RUN apt-get -y upgrade

COPY ./requirements.txt /spreadsheet/requirements.txt
WORKDIR /spreadsheet

RUN python3.9 -m pip install -r requirements.txt

COPY ./spreadsheet /spreadsheet

EXPOSE 6402

ENV PYTHONPATH="/spreadsheet"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
