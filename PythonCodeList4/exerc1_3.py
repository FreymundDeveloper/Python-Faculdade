l = []
c = 0
x = 0

while c < 5:
    l.append(int(input('Digite um valor:')))
    c = c + 1

while x < 5:
    if l[x] % 2 != 0:
        print(l[x])

    x += 1
