s = input("Введите число и символ через пробел: ").split()
size = int(s[0])
symb = str(s[1])

for i in range(1, size + 1):
        if i <= (size + 1) // 2:
            print(symb * i)
        else:
            print(symb * (size - i + 1))