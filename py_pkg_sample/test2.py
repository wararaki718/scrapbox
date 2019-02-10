import hello

def read_txt():
    with open('text.txt') as f:
        print(f.read())

hello.hello_call({'param': 1, 'filepath': 'test.txt'})
read_txt()

hello.hello_call({'param': 2, 'filepath': 'test.txt'})
read_txt()

print("DONE")