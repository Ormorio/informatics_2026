s = input('формат ввода: "число текст"')
N = s[1]
s = s[2:]
l = len(s)
m = [s[i:i+3][::-1] for i in range(0, l, 3)]
print(m)
