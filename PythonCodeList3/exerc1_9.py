di=float(input('Digite o deposito inicial:'))
tj=float(input('digite a taxa de juros:'))

mi=1
mf=12
rsp=0

while mi <= mf:
    di=(di/100*tj+di)
    print('mes', mi, 'valor',di)
    mi=mi+1

print('valor final=', di)
