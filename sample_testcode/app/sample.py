'''
sample class
'''

class Sample(object):
    def __init__(self):
        pass

    def message(self):
        return 'hello'

if __name__ == "__main__":
    sample = Sample()
    print(sample.message())
