def alg(a, b):
    if b == 0:
        return 1, 0, a
    
    x1, y1, d = alg(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return x, y, d

s = input("Введите 2 числа через пробел: ").split()
a = int(s[0])
b = int(s[1])

x, y, d = alg(a, b)

print(f"{x} {y} {d}")