FROM python:3.7

# setup mecab
RUN apt update && \
    apt install -y git sudo mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 && \
    rm -rf /var/lib/apt/lists/*

# setup neologd
RUN git clone https://github.com/neologd/mecab-ipadic-neologd -b v0.0.6 && \
    ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y && \
    rm -rf mecab-ipadic-neologd

# setup python
WORKDIR /work
COPY requirements.txt /work/requirements.txt
RUN pip install -r requirements.txt

# copy codes
COPY sample.py /work/sample.py

CMD ["python", "sample.py"]
