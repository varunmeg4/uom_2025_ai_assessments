def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product(digits):
    max_num = 10**digits - 1
    min_num = 10**(digits - 1)
    largest_palindrome = 0

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

print(largest_palindrome_product(3))