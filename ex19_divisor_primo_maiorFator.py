def eh_primo(num):
    
    primo = False
    if (num != 2 ) and (num % 2 ==0): 
        
        primo = False
        
    
            
    elif (num !=3) and (num % 3 == 0):
        
        primo = False
        
        
    
    elif (num !=5) and (num % 5 == 0):
        
        primo = False
        
        
    else:
    
        primo = True

    return  primo    
        
    
def divisores(num):
    cont = 1
    divisores =  [] 
    while cont <= num:
        if num % cont == 0:
            divisores.append(str(cont))
        cont += 1

    return divisores


def maior_fator_primo(num):
    teste = 0  
    array = divisores(num)
    divisorPrimo = False
    
    for l in range(len(array)-1, -1, -1):
        maiorDivisorPrimo = 0
        teste = int(array[l])
        divisorPrimo = eh_primo(teste)
        if divisorPrimo == True:
            if teste > maiorDivisorPrimo:
                maiorDivisorPrimo = teste
                break

    return maiorDivisorPrimo   
             
        

    

num = int(input('digite  um numero: '))
print(f'{maior_fator_primo(num)} é o maior fator primo ')
print('-=' *10)

#está rodando, teste com 11 (maior divisor é ele mesmo, pois ele é primo), e 10((maiorDivisorPrimo == 5)divisores são 1,2,5,e 10)