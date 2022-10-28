def desvio_padrao(vetor):
    media = sum(vetor) / len(vetor)
    desvioPadrao = 0
    somaVariancia = 0
    for i in range(0,len(vetor)):
        somaVariancia += (vetor[i] - media) ** 2
    
        
    
    desvioPadrao = (somaVariancia / len(vetor)) ** 0.5
    return desvioPadrao

quantidade = 0
vetor = []
num = 0
cont = 1 
quantidade = input('digite a quantidade de itens que você deseja adicionar no vetor')
if quantidade.isdigit() and int(quantidade) > 0:
    quantidade = int(quantidade)
    while cont <= quantidade:
        num = input('digite um numero para adicoonar no vetor: ')
        if num.isdigit():
            num = int(num)
            vetor.append(num)
            cont += 1
           

        else:
            print('digite um numero válido')
    
    print(f'O desvio padrão é {desvio_padrao(vetor)}')
else:
    print('digite uma quantidade válida')

