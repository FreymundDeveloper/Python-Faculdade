import math

a=float(input('Digite um numero: '))
b=float(input('Digite um numero: '))
c=float(input('Digite um numero: '))

raiz=(b**2)-(4*a*c)

if raiz>=0:
    p=math.sqrt(raiz)

    rsp1=(-b+p)/(2*a)
    rsp2=(-b-p)/(2*a)

    print('S={ %.f , %.f }' % (rsp1, rsp2))

else:
    print('Não é possivel tirar a raiz de numeros negativos')
