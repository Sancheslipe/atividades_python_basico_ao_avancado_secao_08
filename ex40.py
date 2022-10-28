def pares_em_vetor(vetor):
    lista = vetor[:]
    contPar = 0
    for i in range(0,len(lista)):
        if lista[i] %2 == 0:
            contPar += 1
        
    return contPar
vetor = []
num = 0
executar = True
while executar == True:
    
    print('deseja adicionar mais um numero? [S] para sim [N] para não:')
    rodar = input('Digite aqui sua resposta: ')
    if rodar.upper() == 'S':
        num = input('digite o numero que você deseja adicionar: ')
        if num.isdigit():
            num = int(num)
            vetor.append(num)
        else:
            print('digite  um numero válido')
    else:
        executar = False
print(f'o vetor é {vetor}')    
print(f'o total de numeros pares é {pares_em_vetor(vetor)}')