with open("input.txt", "r") as f:
    l = f.read()

c = ""
for i in range(len(l) - 1):
    if l[i] in "уеёыаоэяию" and not(l[i + 1] in "уеёыаоэяию") and c != "":
        c = l[i]
        l = f"{l[:i]} 'с' {c} {l[i+1:]}"
    elif l[i] in "уеёыаоэяию" and l[i - 1] in "йцкнгшщзхъфвпрлджчсмтьб" and c != "":
        c = l[i]
        l = f"{l[:i]} 'с' {c} {l[i+1:]}"

if l[-1] in "уеёыаоэяию" and c != "":
    c = l[-1]
    l = f"{l[:-1]} 'с' {c}"


with open("input.txt", "w") as f:
    f.write(l)