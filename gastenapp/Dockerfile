ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install \
    --no-cache-dir \
    --break-system-packages \
    -r /tmp/requirements.txt

WORKDIR /app

COPY . /app

COPY run.sh /etc/services.d/gastenapp/run

RUN chmod a+x /etc/services.d/gastenapp/run
