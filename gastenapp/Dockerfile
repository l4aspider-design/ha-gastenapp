ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install \
    --no-cache-dir \
    --break-system-packages \
    -r /tmp/requirements.txt

COPY app.py /app/app.py
COPY run.sh /etc/services.d/gastenapp/run

RUN chmod a+x /etc/services.d/gastenapp/run
