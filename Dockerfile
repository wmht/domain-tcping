FROM python:3.7.8-slim

WORKDIR /opt
COPY / /opt/
RUN python3 -m pip install --upgrade pip &&\
    pip3 install -r /opt/requirements.txt -i https://mirrors.aliyun.com/pypi/simple &&\
    chmod +x /opt/tools/*

ENTRYPOINT python3.7 main.py