def fatorial(num):
    calc = 1
    cont = int(num)

    for i in range(1, cont+1):
        calc *= i * 1

    return calc

def num_neperiano(num):
    cont = int(num)
    resultado = 0
    for i in range(1,cont):
        resultado += 1 / fatorial(i)
        
    
    return resultado


num = input('digite o numero referente ao ultimo valor fatorial que deseja: ')
if num.isdigit():
    num = int(num)
else:
    print('digite um numero válido!')

print(f' o numero neperiano de 0, até {num} é {num_neperiano(num)}')