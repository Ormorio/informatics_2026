s = input("Введите строку: ").split()

m = 0
n = s[0]

for i in s:
    if s.count(i) > m:
        m = s.count(i)
        n = i

print(n)
