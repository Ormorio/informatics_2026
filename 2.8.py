N = int(input("Введите число: "))
s = input("Введите строку: ").split()

for i in s:
    m = 0
    for j in s:
        if int(j) < int(i):
            m += 1

    if m == N // 2:
        print(i)
        break