from Revisão.Exer4.Revisaoexer4 import STR

teste = STR()

while True:
    s = input('Digite uma string(E para sair):')
    if s is 'E':
        break
    else:
        teste.ial(s)

while True:
    print('1)Imprimir somente as strings com determinada letra;\n'
          '2)Ordem Crescente;\n'
          '3)Ordem Decrescente;\n'
          '4)Sair:')
    x = int(input())

    if x is 4:
        break
    elif x is 1:
        lt = input('Digite uma letra:')
        lf = teste.filt(lt.lower())
        if len(lf) > 0:
            for e in lf:
                print(e)
        else:
            print('Nenhuma string com esta letra inicial encontrada')

    elif x is 2:
        c = teste.oc()
        for x in c:
            print(x)

    elif x is 3:
        d = teste.od()
        for x in d:
            print(x)
