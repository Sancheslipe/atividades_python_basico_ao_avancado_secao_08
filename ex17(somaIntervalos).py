def soma_intervalo(num1,num2):
    somaIntervalo = 0
    if num1 > num2:
        for l in range(num2+1 , num1):
            somaIntervalo += l
        
        return somaIntervalo
    
    elif num2 > num1:
        for l in range(num1 +1 , num2):
            somaIntervalo+= l
        
        return somaIntervalo

    if num1 == num2:
        return print(num1 * 2)


n1 = input('digite o numero 1: ')
if n1.isdigit() and int(n1) > 0:
    n1 = int(n1)
    n2 = input('digite o numero 1: ')
    if n2.isdigit() and int(n2) > 0:
        n2 = int(n2)

        print(soma_intervalo(n1,n2))

    else:
        print('digite um numero válido')    

else:
    print('digite um numero válido')


    
