FROM python:3.9.2-alpine

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /src

CMD python server.py
