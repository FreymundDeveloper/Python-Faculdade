num1=float(input('Digite um numero: '))
num2=float(input('Digite um numero'))
op=str(input('Digite uma forma de operação'))

def resp():
    print('Resultado %.f' % rsp)

if op=='+':
    rsp=num1+num2
    resp()
elif op=='-':
    rsp=num1-num2
    resp()
elif op=='*':
    rsp=num1*num2
    resp()
elif op=='/':
    if num1 and num2 != 0:
        rsp=num1/num2
        resp()
    else:
        print('invalido...Divisão por zero')
