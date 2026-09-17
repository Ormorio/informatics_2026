with open("input.txt", "r") as f:
    l = f.read().strip()

c = 1
for i in range(len(l)-1):
    if l[i] in ".!?":
        if l[i + 1] == " " or l[i + 1] == "\n":
            c += 1
print(c)