from math import *

#N1
"""a = int(input("Enter number a"))
b = int(input("Enter number b"))
c = str(a + b)
d = str(a * b)
print("Sum " + c)
print("Mult " + d)"""

#N2
"""A = input("Enter number")
print(A[-1])"""

#N3
"""a = input("Enter 2 numbers with space")
b = int(a[:a.find(" ")])
c = int(a[a.find(" "):])
d = sqrt(b*c)
print(d)"""

#N4
"""f = open("input.txt")
F = f.read().split(" ")
f.close()
a = F[-1][-1]
#print(a)
F[-1] = F[-1][:len(F[-1]) - 2]
#print(F)
m = int(F[0])
for k in F[1:]:
    if a == "+":
        m += int(k)
    elif a == "*":
        m *= int(k)
    elif a == "-":
        m -= int(k)
print(m)
f = open("output.txt", "w")
f.write(str(n))
f.close()"""

#N5
"""N = str(1670)
b = 8
c = 5
n = ''
N = int(N,b)

while N > 0:
    n = n[::-1]
    n += str(N % c)
    n = n[::-1]
    N = N // c

print(n)"""

#N6
f = open("input.txt.txt")
f1 = f.readline().split(" ")
f2 = f.readline()[0]
f3 = int(f.readline())
f1[-1] = f1[-1][:len(f1[-1]) - 1]
f.close()

print(f1)

for f in range(len(f1)):
    f1[f] = int(f1[f],f3)

print(f1)
print(f2)

m = int(f1[0])
for k in f1[1:]:
    if f2 == "+":
        m += int(k)
    elif f2 == "*":
        m *= int(k)
    elif f2 == "-":
        m -= int(k)
print(m)

n = ''
while m > 0:
    n = n[::-1]
    n += str(m % f3)
    n = n[::-1]
    m = m // f3
print(n)

f = open("output.txt", "w")
f.write(str(n))
f.close()
