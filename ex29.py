def fatorial(num):
    calc = 1
    cont = int(num)

    for i in range(1, cont+1):
        calc *= i*1

    return calc


def serie_de_taylor_seno_hiperbolico(num):
    angulo = (num * 3.141593)/ 180
    resultado = []
    calculo = 0
    for n in range(0, 5+1):
        seno = ((angulo **(2 * n +1) ) / fatorial((2 * n +1)))

        print(f'{seno} este é o resultado da expressão angulo **{(2 * n +1)} / {2*n + 1}! ')
        resultado.append(seno)

     
    for i in range(0, len(resultado)):
        if i % 2 == 0:
            calculo += angulo ** resultado[i] /fatorial(resultado[i])
        else:
            calculo -= angulo ** resultado[i] / fatorial(resultado[i])
    
    return calculo


num = input('digite um angulo em graus: ')
if num.replace('.','', 1).isdigit():
    num = float(num)

    print(f' X =  {serie_de_taylor_seno_hiperbolico(num)}')

else:
    print('digite  um numero válido!')