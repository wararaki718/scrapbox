FROM python:3.6

COPY requirements.txt /work/requirements.txt

WORKDIR /work
RUN pip install -r requirements.txt

COPY app.py /work/app.py

CMD ["python", "app.py"]
