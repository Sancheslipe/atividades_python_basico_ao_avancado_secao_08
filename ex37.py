def hiperfatorial(num):
    cont = int(num)
    hiperFatorial = 0
    for n in range(1, cont+1):
        
        # print(f'({n- 1} ** {n-1}) * ({n} ** {n})') #testando para ver se a formula estava certa
        hiperFatorial = ((n-1) ** n-1) * (n **n)
    return hiperFatorial


num = input('digite  um numero: ')
if num.isdigit():
    num = int(num)
    print(hiperfatorial(num))
else:
    print('digite um numero valido! ')