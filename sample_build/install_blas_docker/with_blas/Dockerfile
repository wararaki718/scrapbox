FROM python:3.6

# setup blas
RUN apt update && apt upgrade -y && \
    apt install -y unzip
RUN cd /usr/local/src && wget https://github.com/xianyi/OpenBLAS/archive/v0.3.4.zip && \
    unzip v0.3.4.zip && cd OpenBLAS-0.3.4 && \
    make -j 4 && make PREFIX=/usr/local install && \
    rm -rf /usr/local/src/OpenBLAS-0.3.4

# test
RUN pip install Theano==1.0.4 pymc3==3.6

WORKDIR /work
COPY check.py /work/check.py

CMD ["python", "check.py"]
