FROM ubuntu:18.04

RUN export LC_ALL=C.UTF-8 \
    && export LANG=C.UTF-8

RUN apt update && apt install -y python3-dev python3-pip git \
    && pip3 install pipenv

RUN git clone https://github.com/aviboppana/PennApps2018 
WORKDIR PennApps2018 
RUN git checkout production

RUN pipenv install 
RUN python app.py runserver

EXPOSE 8080

