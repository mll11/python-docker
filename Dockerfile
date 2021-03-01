FROM python:3.9.2-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./server.py" ] 
