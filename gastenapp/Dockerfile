ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install \
    --no-cache-dir \
    --break-system-packages \
    -r /tmp/requirements.txt

WORKDIR /app

COPY app.py /app/app.py
COPY run.sh /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
