FROM python:3.11-alpine AS build
WORKDIR /app

RUN apk add nodejs npm
RUN npm i -g nodemon
COPY ./src /app/src/
COPY render.yaml /app/render.yaml
COPY laucher.py /app/laucher.py
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["nodemon", "laucher.py"]
RUN python app.py
