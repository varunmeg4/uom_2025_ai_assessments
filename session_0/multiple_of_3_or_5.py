def sum_of_multiples(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

result = sum_of_multiples(1000)
print(result)