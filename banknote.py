N = 120
a = [10, 60, 100]

cash_sums = {0, 0} # summ: last banknote
for note_number in range(N // a[0] + 1):
    current_sums = list(cash_sums.keys())
    for sum in current_sums:
        for note in a:
            if sum + note not in cash_sums and sum + note <= N:
                cash_sums[sum + note] = note

if N in cash_sums:
    print("Yes")
    result_notes = {note: 0 for note in a}
    while N > 0:
        result_notes[cash_sums[N]] += 1
        N -= cash_sums[N]
    print(result_notes)
else:
    print("No")