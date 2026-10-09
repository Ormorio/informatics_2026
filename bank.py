W = 45
n = 6
p = [1, 2, 3, 5, 8, 90]
w = [1, 2, 3, 7, 19, 100]
P = [[0 for j in range(W + 1)] for i in range(n + 1)]
sp = []

for k in range(1, n + 1):
    for S in range(1, W + 1):
        if S - w[k - 1] >= 0:
            P[k][S] = max(p[k-1] + P[k - 1][S - w[k - 1]], P[k - 1][S])
        else:
            P[k][S] = P[k - 1][S]

S = W
k = n
while k > 0:
    if P[k][S] != P[k - 1][S]:
        sp.append(k)
        S -= w[k - 1]
        k -= 1
    else:
        k -= 1

print(P[-1][-1])
print(sp)