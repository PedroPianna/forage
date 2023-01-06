FROM ubuntu:22.04
WORKDIR /home/

RUN apt-get update -y
RUN apt install pip -y
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt 

RUN python3 -m pip install -r requirements.txt
