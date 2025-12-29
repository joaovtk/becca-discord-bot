FROM python:3.11-alpine AS build
WORKDIR /app

COPY ./src /app/src/
COPY render.yaml /app/render.yaml
COPY laucher.py /app/laucher.py
COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "laucher.py"]
RUN python app.py
