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

def primo_abaixo_de_num(num):
    primos = []
    for i in range(2,num+1):
        if eh_primo(i) == True:
            primos.append(i)
    
    return primos

num = input('digite um numero: ')
if num.isdigit():
    num = int(num)
    print(primo_abaixo_de_num(num))

else:
    print('digite um nnumero válido')