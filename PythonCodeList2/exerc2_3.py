n=str(input('Digite o nome do produto: '))
v=float(input('Digite o valor do produto: '))

if v<10:
    rsp=v*0.7+v
elif 10 <= v < 30:
    rsp=v*0.5+v
elif 30<= v <50:
    rsp=v*0.4+v
elif v>50:
    rsp=v*0.3+v

print('%.s lucro de  R$ %.2f' % (n, rsp))
