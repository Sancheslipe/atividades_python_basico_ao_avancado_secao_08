def maior(vetor):
    lista = vetor[:]
    maiornum = 0

    for l in range(0,len(vetor)):
        if vetor[l] > maiornum:
            maiornum = vetor[l]
        
    return maiornum

vetor = []
executar = True
rodar = ''
num = 0

while executar == True:
    print(' deseja adicionar um numero? [S] para sim [N] para não\n')
    rodar = input('digite aqui a sua resposta: ')
    if rodar.upper() == 'S':
        num = input('digite aqui o numero que você deseja adicionar: ')
        if num.isdigit():
            num = int(num)

            vetor.append(num)
        else:
            print('digite um numero válido')
    else:
        executar = False

print(f'\n o vetor é {vetor}')
print(f' o maior numero é {maior(vetor)}')