def matriz_transposta(matriz):
    transposta = [[],[],[]]
    
    for l in range(0,3):
        for c in range(0,3):
            transposta[c].append(matriz[l][c])

    return transposta



matriz = [[],[],[]]
transposta = list()
num = 0 
l = 0
c = 0

while l < 3:
    while c < 3:
        num = input('digite um numero: ')
        if num.isdigit():
            num = int(num)
            matriz[l].append(num)
            c += 1
        else:
            c= c
            print('digite um numero válido')
    l += 1
    c = 0

transposta = matriz_transposta(matriz)


print('\nA matriz é \n')
for l in range(0,3):  
    for c in range(0,3):
        print(f'{matriz[l][c]}', end=' ')
    print()

print('\nA transposta é \n')
for l in range(0,3):  
    for c in range(0,3):
        print(f'{transposta[l][c]}', end=' ')
    print()