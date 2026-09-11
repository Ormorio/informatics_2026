a = list(map(int, input().split()))
print(a)

n = a[0]
del(a[0])

a.sort()
print(a, n)

c = 0
for b in a:
    if b == c:
        c += 1
    else:
        print(c)
        break