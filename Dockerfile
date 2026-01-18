FROM alpine AS build

WORKDIR /app
RUN apk add --no-cache python3 py3-pip
COPY requirements.txt /app/requirements.txt
ENTRYPOINT [ "python", "-m", "venv", "venv"]
COPY venv /app/venv
RUN source venv/bin/activate

RUN pip install -r requirements.txt
RUN python src/app.py 