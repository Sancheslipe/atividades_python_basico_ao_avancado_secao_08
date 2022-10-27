def pontencializacao(base,expoente):
    result = base ** expoente   
    return result


numBase = input('digite o numero que será a base da potenciação: ')
if numBase.replace('.','', 1).replace('-','').isdigit():
    numBase = float(numBase)
    expoente = input('digite o numero que será a potencia: ')
    if expoente.replace('.','', 1).isdigit():
        expoente = float(expoente)

        print(pontencializacao(numBase,expoente))

    else:
        print('digite um numero válido')
else:
    print('digite um numero válido')