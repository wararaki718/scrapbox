FROM python:3.6

WORKDIR /work
COPY api.py /work
COPY requirements.txt /work

RUN pip install -r requirements.txt

CMD ["python", "api.py"]
