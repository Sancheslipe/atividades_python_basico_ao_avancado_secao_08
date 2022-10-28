def soma_diagonal_principal(matriz):
    soma = 0
    for l in range(0,3):
        for c in range(0,3):
            if (l == 0 and c  == 0) :
                soma += matriz[l][c]
                
            elif l == 1 and c == 1:
                soma += matriz[l][c]
                
            elif l == 2 and c == 2:
                soma += matriz[l][c]
                

    return soma
matriz = [[],[],[]]
l = 0
c = 0
num = 0

while l <3:
    while c <3:
        num = input('digite um numero: ') 
        if num.isdigit():
            num = int(num)
            matriz[l].append(num)
            c +=1

        else:
            c = c
            print('digite um numero válido')
    l+=1
    c = 0


print('-='*35)
print('\nA matriz é \n')
for l in range(0,3):  
    for c in range(0,3):
        print(f'{matriz[l][c]}', end=' ')
    print()

print(f'\ne a soma dos numeros na diagonal principal é {soma_diagonal_principal(matriz)}')