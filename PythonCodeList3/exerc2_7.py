c=0
op=1
tt=0

while op != 0:
    op=float(input('Digite um numero:'))

    tt=tt+op
    c=c+1

print('Media=', tt/(c-1))
