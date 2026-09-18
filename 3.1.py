n = int(input('Введите число: '))
n0 = 0
n1 = 1
def fib(n):
    global n0, n1
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        for i in range(2, n + 1):
            n0, n1 = n1, n0 + n1
        return n1
print(fib(n))