def is_odd(n):
    return n % 2 == 1

num =1
is_not_found = True
while is_not_found:
    for i in range(1, num):
        if is_odd(i) or is_odd(num):
            a = num**2 - i**2
            b = 2*i*num
            c = num**2 + i**2
            if a + b + c == 1000:
                print(a*b*c)
                is_not_found = False
                break
            elif 1000 % (a+b+c) == 0:
                k = 1000//(a+b+c)
                print((k*a)*(k*b)*(k*c))
                is_not_found = False
                break
    num += 1