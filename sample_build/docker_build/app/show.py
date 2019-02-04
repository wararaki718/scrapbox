import sys

def main():
    with open('base.txt') as f:
        print(f.read())
    return 0

if __name__ == '__main__':
    sys.exit(main())
