FROM python:3.8.10
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
CMD ["python3", "app/server.py"]
