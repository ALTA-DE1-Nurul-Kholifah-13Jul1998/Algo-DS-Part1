def primeX(x):
    list_prima = [2,3,5,7,11,13,17,19,23,29]
    index = list_prima[x-1]
    return index

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29