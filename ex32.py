def simplifica(numerador,denominador):
    simplifica = False
    divisor = 0
    menor = 0

    if numerador > denominador:
        menor = int(denominador // 1)
    elif denominador >numerador:
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

        return f'numerador {numerador}, denominador {denominador} numero que os simplificou {divisor}'
    else:
        return 'não foi possivel simplificar!'


num1 = input('digite o numerador que deseja simplificar: ')
if num1.replace('.','', 1).replace('-','').isdigit():
    num1 = float(num1)

    num2 = input('digite o denoinador que deseja simplificar: ')
    if num2.replace('.','', 1).replace('-','').isdigit():
        num2 = float(num2)

        print(simplifica(num1,num2))
        
    else:
        print('digite um denominador válido')
else:
    print('digite um numerador válido')



