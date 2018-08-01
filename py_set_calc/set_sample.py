import sys

def main():
    a = set([1, 2, 3, 4])
    b = set([3, 4, 5, 6])
    print("データ")
    print(f" a={a}")
    print(f" b={b}")
    print("真偽値")
    print(f" a in b={a in b}")
    print(f" a not in b={a not in b}")
    print(f" a.issubset(b)={a.issubset(b)} # a<=bと同じ")
    print(f" a.issuperset(b)={a.issuperset(b)} # a=>bと同じ")
    print("集合演算")
    print(f" a.union(b)={a.union(b)} # a|bと同じ")
    print(f" a.intersection(b)={a.intersection(b)} # a&bと同じ")
    print(f" a.difference(b)={a.difference(b)} # a-bと同じ")
    print(f" a.symmentric_difference(b)={a.symmetric_difference(b)} # a^bと同じ")

    return 0


if __name__ == "__main__":
    sys.exit(main())
