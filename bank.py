W = 4
n = 3
p = [1, 2, 3]
w = [1, 2, 3]
P = [[0 for j in range(W + 1)] for i in range(n + 1)]

for k in range(1, n + 1):
    for S in range(1, W + 1):
        if S - w[k - 1] >= 0:
            P[k][S] = max(p[k-1] + P[k - 1][S - w[k - 1]], P[k - 1][S])
        else:
            P[k][S] = P[k - 1][S]
print(P[-1][-1])