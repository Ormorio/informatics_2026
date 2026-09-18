n = int(input('Введите число: '))
k = []
def raz(n):
    if n == 1:
        return(1)
    for i in range(2, n + 1):
        if n % i == 0:
            if not(i in k):
                k.append(i)
            raz(n // i)
            return(k)
                
print(*(raz(n)))