def media_vetor(vetor):
    lista = vetor[:]
    media = sum(vetor)/ len(vetor)

    return media

vetor = []
num = 0
executar = True
rodar =''
num = 0
while executar == True:
    print('deseja adicionar mais um numero na lista [S] sim [N] Não\n')
    rodar = input('digite aqui a sua resposta:')
    if rodar.upper() == 'S':
        num = input('digite aqui o numero desejado: ')
        if num.replace('.','', 1).replace('-','').isdigit():
            num = float(num)
            vetor.append(num)
        else:
            print('digite um numero válido')
    else:
        executar = False

print(f' o vetor é {vetor}')
print(f' a media do vetor é {media_vetor(vetor)}')
