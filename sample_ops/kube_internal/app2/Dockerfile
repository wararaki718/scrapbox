FROM python:3.7

COPY requirements.txt /work/requirements.txt
COPY api.py /work/api.py
COPY run.sh /work/run.sh

WORKDIR /work
RUN pip install -r requirements.txt

CMD ["sh", "run.sh"]
