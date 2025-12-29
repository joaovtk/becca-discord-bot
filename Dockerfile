FROM python:3.11-alpine AS build
WORKDIR /app

COPY ./src /app/src/
COPY render.yaml /app/render.yaml
COPY laucher.py /app/laucher.py
COPY requirements.txt /app/requirements.txt

RUN pip install virtualenv
RUN python -m venv venv
RUN source venv/bin/activate

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "laucher.py"]
