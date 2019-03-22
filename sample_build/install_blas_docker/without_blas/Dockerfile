FROM python:3.6

# test
RUN pip install Theano==1.0.4 pymc3==3.6

WORKDIR /work
COPY check.py /work/check.py

CMD ["python", "check.py"]
