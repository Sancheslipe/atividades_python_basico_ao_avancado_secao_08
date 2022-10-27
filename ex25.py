def resultado(num):
    S = 0
    cont = int(num)

    for i in range(1, cont+1):
        numerador = (i ** 2) + 1
        denominador =  i + 3
        S += numerador / denominador
    
    return S 

num = input('digite um numero: ')
if num.isdigit():
    num = int(num)
    print(resultado(num))
else:
    print('digite um numero válido')