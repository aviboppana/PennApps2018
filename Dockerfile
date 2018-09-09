ROM ubuntu:18.04

RUN apt update && apt install -y python3-dev python3-pip \
    && pip install pipenv


