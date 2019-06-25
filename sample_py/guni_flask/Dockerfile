FROM python:3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /work
COPY sample.py /work/sample.py

CMD ["gunicorn", "--bind", "0.0.0.0:5555", "sample:app"]
