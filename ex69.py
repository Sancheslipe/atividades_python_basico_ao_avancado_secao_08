

def simplifica(numerador,denominador):
    simplifica = False
    divisor = 0
    menor = 0

    if numerador > denominador:
        menor = int(denominador // 1)
    elif denominador > numerador:
        menor = int(numerador // 1)
    else:
        menor = int(numerador // 1)
    
    for s in range(menor, 1,-1):
        
        if (numerador % s == 0) and denominador % s == 0:
            simplifica = True
            divisor = s
            break
    
    if simplifica == True:
        numerador = numerador / divisor
        denominador = denominador / divisor

        return f'numerador {numerador}, denominador {denominador} o maior divisor é {divisor}'
    else:
        return 'não foi possivel simplificar!'


def soma_fracao(numerador1,denominador1,numerador2,denominador2):
    soma = 0
    maior = 0
    executar = True
    mmc = 0
    denominadorFinal = 0
    numeradorFinal = 0
    if denominador1 == denominador2:
        soma = numerador1 + numerador2
        return soma, denominador1
    else:         
        executar = True
        
        if denominador1 > denominador2:
            maior = denominador1
        else:
            maior = denominador2
        
        while executar == True:
            if maior % denominador1 == 0 and maior % denominador2 == 0:
                mmc = maior
                executar = False
            
            else:
                maior += 1
    denominadorFinal = mmc 
    numeradorFinal = ((mmc / denominador1  ) * numerador1) + ((mmc / denominador2 ) * numerador2)
        
   
    return numeradorFinal, denominadorFinal

def subtracao_fracao(numerador1,denominador1,numerador2,denominador2):
    div = 0
    maior = 0
    executar = True
    mmc = 0
    denominadorFinal = 0
    numeradorFinal = 0
    if denominador1 == denominador2:
        
        div = numerador1 - numerador2
        return div, denominador1
    else:         
        executar = True
        
        if denominador1 > denominador2:
            maior = denominador1
        else:
            maior = denominador2
        
        while executar == True:
            if maior % denominador1 == 0 and maior % denominador2 == 0:
                mmc = maior
                executar = False
            
            else:
                maior += 1
        
    denominadorFinal = mmc 
        
    
    numeradorFinal = ((mmc / denominador1 ) * numerador1) - ((mmc / denominador2  ) * numerador2)
    return numeradorFinal, denominadorFinal



        
def multiplicacao_fracao(numerador1 ,numerador2  , denominador1 = 1 , denominador2 = 1):
    denominadorFinal = denominador1 * denominador2
    numeradorFinal = numerador1 * numerador2

    return numeradorFinal, denominadorFinal

def divisao_fracao(numerador1 ,numerador2  , denominador1 = 1 , denominador2 = 1):
    denominadorFinal = denominador1 * numerador2
    numeradorFinal = numerador1 * denominador2
    return numeradorFinal, denominadorFinal


n1 = 0
n2 = 0
d1 = 0
d2 = 0


n1 = input('digite um numerador: ')
if n1.isdigit():
    n1 = int(n1)
    
    n2 = input('digite um numerador: ')    
    if n2.isdigit():
        n2 = int(n2)
        
        d1 = input('digite um denominador')       
        if d1.isdigit():
            d1 = int(d1)
              
            d2 = input('digite um denominador')
            if d2.isdigit():
                d2 = int(d2)
        
         
            
            else:
                print('digite um numero válido')
        
        
        else:
            print('digite um numero válido')
   
    else:
        print('digite um numero válido')

else:
    print('digite um numero válido')

print('\nsimplificação 1\n')
print(simplifica(n1,d1))

print('\nsimplificação 2\n')
print(simplifica(n2,d2))

print('\nsoma\n')
print(soma_fracao(n1,d1,n2,d2))

print('\nsubtração\n')
print(subtracao_fracao(n1,d1,n2,d2))

print('\ndivisão\n')              # o "int()" é só para o programa parar de berrar erro, funciona sem, só que fica vermelho 
print(divisao_fracao(n1,n2,int(d1),int(d2)))

print('\nmultiplicação\n')
print(multiplicacao_fracao(n1,n2,int(d1),int(d2)))