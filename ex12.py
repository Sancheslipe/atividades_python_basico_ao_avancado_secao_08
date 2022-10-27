def soma_algarismos(numero):
    somaAlgarismo = 0
    cont = int(numero)

    if cont > 0:
        numero = str(numero)
        
        for c in range(0, len(numero) ):
            
            somaAlgarismo += int(numero[c])

        return print(somaAlgarismo)
    return numero


num = input('digite um numero: ')
if num.isdigit() and int(num) > 0:
    num = int(num)
    soma_algarismos(num)
else:
    print('digite um numero válido!')
    
