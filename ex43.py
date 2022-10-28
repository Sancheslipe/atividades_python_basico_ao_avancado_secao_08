import random


def preencher_aleatorio(vetor,quantidade):
    numAleatorio = 0
    lista = vetor[:]
    for l in range(1, quantidade +1):
        numAleatorio = (random.randint(0,99))
        if numAleatorio not in lista:
            lista.append(numAleatorio)
        else:
            numAleatorio = (random.randint(0,99))
            lista.append(numAleatorio)
        
    return lista

vetor = []
num = 0
executar = True
cont = 1

quantidade = input('digite a quantidde de numeros aleatórios que você deseja adicionar no vetor: ')
if quantidade.isdigit():
    quantidade = int(quantidade)
    

    print(f'este é o vetor preenchido {preencher_aleatorio(vetor,quantidade)}')

else:
    print('digite uma quantidade válida')
