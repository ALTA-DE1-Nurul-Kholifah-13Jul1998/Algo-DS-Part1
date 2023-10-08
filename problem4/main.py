def is_prime(num):
    if num<=1:
        return False
    for i in range(2, num):
        if num%i==0:
            return False
    return True  

def generate_primes_grid(width, height, start):
    result = ""
    bil_prima = start+1
    for i in range(height):
        mat_prima = []
        for j in range(width):
            while not is_prime(bil_prima): #cek prima, +1 jika bukan bilangan prima
                bil_prima += 1
            mat_prima.append(bil_prima)
            bil_prima += 1
            
        max_prime = max(mat_prima)
        max_width = len(str(max_prime))  #meghitung len maks dari bil prima untuk ditambahkan spasi pada digit kurang dari maks bil prima 

        formatted_row = ["{:<{width}}".format(prime, width=max_width) for prime in mat_prima] 
        result += " ".join(formatted_row) + "\n"
    return result


if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """