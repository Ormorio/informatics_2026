a = list(map(int, input().split()))
print(a)

n = a[0]
del(a[0])

a.sort()
print(a, n)

b = 0
for b in range(len(a)):
    if a[b] == b:
        b += 1
    else:
        print(b)
        break