def calculate_sum_square_diff(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares

print(calculate_sum_square_diff(100))