s = input("Введите строку: ").split()
print(*(x for x in s if s.count(x) == 1))