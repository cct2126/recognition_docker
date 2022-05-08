FROM python:3.8.10
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python3", "app/server.py"]
