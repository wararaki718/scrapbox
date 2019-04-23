import gzip
from io import StringIO, BytesIO
import sys

import pandas as pd


def test_byte():
    print('gzip write&read check:')
    bdata = BytesIO()

    with gzip.open(bdata, 'wb') as f:
        f.write(b'byte test\n')
    print('write:')

    bdata.seek(0)
    with gzip.open(bdata, 'rb') as f:
        print(f.read())
    print('read:')


def test_string():
    print('string write&read check:')
    sdata = StringIO(
        '''
        id,name
        1,test
        2,hello
        3,world
        '''
    )
    df = pd.read_csv(sdata)
    print(df)

    with StringIO() as f:
        f.write(df.to_csv())
        print(f.getvalue())


def main():
    test_byte()
    print('\n')
    test_string()

    return 0


if __name__ == '__main__':
    sys.exit(main())
