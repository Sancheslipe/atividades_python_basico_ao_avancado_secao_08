def soma_coluna_matriz(matriz, coluna):
    soma = 0
    for l in range(0,7):
        for c in range(0,6):
            
            if coluna == c:
                soma += matriz[l][c]
    
    return soma


matriz = [[],[],[],[],[],[],[]]
linha = 0
coluna = 0
num = 0
colunaSoma = 0
soma = 0

while linha < 7:
    while coluna < 6:
        num = input(f' digite um numero referente á {linha},{coluna}: ')
        if num.replace('.','', 1 ).replace('-',''):
            num = float(num)
            matriz[linha].append(num)
            coluna += 1


        else:
            coluna = coluna
            print(' digite um numero válido!')
    linha += 1 
    coluna = 0

linha = 0

while linha <1:
    colunaSoma = input(' digite o numero da coluna que você deseja fazer a soma dos valores: ')
    if colunaSoma.isdigit():
        colunaSoma = int(colunaSoma)
        linha += 1 
    else:
        linha = linha
        print('digite um numero válido')

soma = soma_coluna_matriz(matriz, colunaSoma)

print(f' a soma dos itens na linha {colunaSoma} é {soma}')