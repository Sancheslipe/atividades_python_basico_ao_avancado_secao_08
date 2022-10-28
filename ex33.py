def fatorial(num):
    calc = 1
    cont = int(num)

    for i in range(1, cont+1):
        calc *= i*1

    return calc

def soma_algarismo_fatorial(num):
    cont = fatorial(int(num))
    numero = str(cont)
    somaAlgarismos = 0

    if len(numero) > 0:

        for c in range(0, len(numero)):
            somaAlgarismos += int(numero[c])
        
        return f'o fatorial é {cont} a soma dos algarismos é {somaAlgarismos}'
   

num = input('digite um numero: ')
if num.isdigit():
    num = int(num)

    print(soma_algarismo_fatorial(num))

else:
    print('digite um numero válido')
