with open("input.txt", "r") as f:
    l = f.read().strip()

alph = "QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
c = 1
for i in range(1, len(l)-1):
    if l[i] in ".!?":
        if l[i + 1] == " " or l[i + 1] == "\n":
            if l[i - 1] in alph and l[i - 2] in alph:
                continue
            elif len(l) - i - 2 > 0 and not(l[i + 2] in alph):
                continue
            else:
                c += 1
print(c)