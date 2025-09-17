def even_fibonacci_sum(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

if __name__ == "__main__":
    print(even_fibonacci_sum(4000000))