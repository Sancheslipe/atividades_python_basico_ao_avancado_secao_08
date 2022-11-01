def soma_linha_matriz(matriz, linha):
    soma = 0
    for l in range(0,7):
        for c in range(0,6):
            
            if linha == l:
                soma += matriz[l][c]
    
    return soma


matriz = [[],[],[],[],[],[],[]]
linha = 0
coluna = 0
num = 0
linhaSoma = 0
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
    linhaSoma = input(' digite o numero da linha que você deseja fazer a soma dos valores: ')
    if linhaSoma.isdigit():
        linhaSoma = int(linhaSoma)
        linha += 1 
    else:
        linha = linha
        print('digite um numero válido')

soma = soma_linha_matriz(matriz, linhaSoma)

print(f' a soma dos itens na linha {linhaSoma} é {soma}')