FROM python:3.6

WORKDIR /work
COPY app.py /work
COPY requirements.txt /work

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
