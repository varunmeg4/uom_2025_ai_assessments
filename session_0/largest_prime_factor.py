def main():
    n = 600851475143
    print(largest_prime_factor(n))
    pass

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    for i in range(n+1 , 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    

main()

"""def largest_prime_factor(n):
    factor = 2
    last_factor = 1
    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return last_factor

largest_prime_factor(600851475143)
"""

