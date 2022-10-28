def fatorial(num):
    calc = 1
    cont = int(num)

    for i in range(1, cont+1):
        calc *= i*1

    return calc

def super_fatorial(num):
    cont = int(num)
    superFatorial = 1
    for c in range(0, cont+1):
        superFatorial *= fatorial(c)
    
    return superFatorial

num = input(' digite um numero: ')
if num.isdigit():
    num = int(num)
    print(super_fatorial(num))
else:
    print('digite um numero válido!')