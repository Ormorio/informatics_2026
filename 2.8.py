N = int(input("Введите число: "))
s = input("Введите строку: ").split()

for i in s:
    m = 0
    for j in s:
        if int(j) < int(i):
            m += 1

    if m - s.count(i) + 1 <= N // 2 <= m + s.count(i) - 1:
        print(i)
        break