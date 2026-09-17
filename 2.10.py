with open("input.txt", "r") as f:
    l = f.read()

c = ""
k = ""
for i in range(len(l)):
        if l[i] in "уеёыаоэяиюУЕЁЫАОЭЯИЮ" and c == "":
            c = l[i]
            break

for i in range(len(l)):
    k += l[i]
    if i  > 0 and l[i] in "уеёыаоэяиюУЕЁЫАОЭЯИЮ" and l[i - 1] in "йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ" and c != "":
        c = l[i]
        k += "с" + c.lower()

with open("input.txt", "w") as f:
    f.write(k)