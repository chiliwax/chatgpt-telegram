FROM python:3.9-slim

WORKDIR /app

#raspberry only (look like)
RUN apt-get update
RUN apt-get -y install curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN chmod +x rust.sh;./rust.sh -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]