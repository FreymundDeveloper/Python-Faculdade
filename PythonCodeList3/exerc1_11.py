num=1
t=0
n=0

while num != 0:
    num=int(input('Digite um numero:'))
    n=n+num
    t=t+1

print('Quantidade de numeros digitados=', t)
print('Soma=', n)
print('Media=', n/t)
