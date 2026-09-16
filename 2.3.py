s  = input("Введите строку: ")
p = False

if s == s[::-1]:
    p = True    

a = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 
    'Y': 'Y', '1': '1', '8': '8',
    'E': '3', '3': 'E',
    'J': 'L', 'L': 'J',
    'S': '2', '2': 'S',
    'Z': '5', '5': 'Z'
}
z = True
for i in range(len(s)):
    if s[i] not in a or a[s[i]] != s[len(s) - 1 - i]:
        z = False
        break


if not p and not z:
    print(f"{s} is not a palindrome.")
elif p and not z:
    print(f"{s} is a regular palindrome.")
elif not p and z:
    print(f"{s} is a mirrored string.")
elif p and z:
    print(f"{s} is a mirrored palindrome.")