def fatorial(num):
    calc = 1
    cont = int(num)

    for i in range(1, cont+1):
        calc *= i*1

    return calc

def fatorial_quadruplo(num):
    n = int(num)

    calc = fatorial((2 * n)) / fatorial(n)

    return calc

num = input(' digite um numero: ')
if num.isdigit():
    num = int(num)
    print(fatorial_quadruplo(num))
else:
    print('digite um numero válido')

