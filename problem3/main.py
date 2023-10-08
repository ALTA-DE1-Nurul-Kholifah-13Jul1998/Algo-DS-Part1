def fibonacci(number):
    bil_fib = [0, 1]

    if number <= 1:
        return bil_fib[number]
        
    for i in range(2, number+1):
        next_fib = bil_fib[i-1] + bil_fib[i-2]
        bil_fib.append(next_fib)

    return bil_fib[number]

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144