def fatorial_exponencial(num):
    cont = int(num)
    potencia = 1
    fatorialExponencial = 1
    for l in range(1, cont+1):
        
        potencia *= l
        print(potencia)
    
    fatorialExponencial = num ** potencia
    return fatorialExponencial



num = input(' digite um numero: ')
if num.isdigit():
    num = int(num)
    print(fatorial_exponencial(num))
else:
    print('digite um numero válido!')
