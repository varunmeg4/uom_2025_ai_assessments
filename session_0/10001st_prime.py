def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

target_count = 10001
count = 0
n = 1
while count < target_count:
    if is_prime(n):
        count += 1
        if count == target_count:
            print(n)
            break
    n += 1