#fazer uma função que receba 2 matrizes quadradas e devolva o produto matrical

# o numero de colunas da primeira matriz tem que ser igual ao numero de linhas da segunda,
#  caso contrário a resposta será vazia, impossivel de calcular

#pegar a quantidade de linhas da primeira (para ser o numero de linhas)
#pegar a quantidade de colunas da segunda( para ser as colunas)

# para fazer o produto, pega os itens da primeira linha da matriz 1 vezes a primeira e a segunda linha,
#  para serem os itens da primeira linha 

# repetir o processo para pegar os 2 itens

def produto_matrical(ordem,matriz1,matriz2Transposta):
    matrizC = []
    soma = 0
    for i in range(0,ordem):
        matrizC.append([])
    
    for l in range(0,ordem):
        for c in range(0,ordem):
            soma = matriz1[l][c] * matriz2Transposta[l][c]
            matrizC[l].append(soma)
    
    return matrizC



num = 0

prodMatrical = 0 
matrizA = [] 
matrizB = []
matrizC = []
col = []
linha = 0
line = 0
col = 0


linha = int(input('digite o numero de linhas que você deseja ter'))

for l in range(0,linha):
    matrizA.append([])
    matrizB.append([])

while line < linha:
    while col < linha:
        num = input(f'digite um numero referente á {line},{col} :')
        if num.replace('.','', 1).replace('-','').isdigit():
            num = float(num)
            matrizA[line].append(num)
            col += 1
        else:
            col = col
            print('digite um numero válido')
    line+= 1
    col = 0


line = 0
col = 0
print('\n')
while line < linha:
    while col < linha:
        num = input(f'digite um numero referente á {line},{col} : ')
        if num.replace('.','', 1).replace('-','').isdigit():
            num = float(num)
            matrizB[col].append(num)
            col += 1
        else:
            col = col
            print('digite um numero válido')
    line+= 1
    col = 0


matrizC = produto_matrical(linha,matrizA,matrizB)



print('\n')
print('matrizA')
print('-='*35)
for l in range(0,linha):
    for c in range(0,linha):
        print(f'{matrizA[l][c]}', end = ' ')
    print()

print('\n')
print('matrizB')
print('-='*35)


for l in range(0,len(matrizB)):
    for c in range(0,linha):
        print(f'{matrizB[l][c]}', end = ' ')
    print()


print('\n')
print('matrizC')
print('-='*35)


for l in range(0,len(matrizC)):
    for c in range(0,linha):
        print(f'{matrizC[l][c]}', end = ' ')
    print()




















