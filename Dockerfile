FROM python:3.8.10
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3", "app/server.py"]