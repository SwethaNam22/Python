def sum_fib(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    summ = 0
    c = 0
    while c < n:
        summ += a
        a, b = b, a + b
        c += 1
    return summ      

n1 = int(input("Enter the value of n: "))
print(sum_fib(n1))