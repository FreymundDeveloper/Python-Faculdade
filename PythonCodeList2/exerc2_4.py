s=float(input('Digite o valor do seu salario: '))

def resp():
    print('O valor do seu saloario com o desconto do INSS será de R$', rsp)

if s<= 600:
    rsp=s
elif s> 600 <= 1200:
    rsp=s-(s*0.2)
elif s> 1200 <= 2000:
    rsp=s-(s*0.25)
elif s> 2000:
    s=s-(s*0.3)

resp()
