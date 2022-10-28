def matriz_maior_que_10(matriz):
    maior10 = 0

    for l in range(0,4):
        for c in range(0,4):
            if matriz[l][c] > 10:
                maior10 +=1
    
    return maior10

matriz =[[],[],[],[]]
num = 0
l = 0
c = 0

while l < 4:
    while c<4:
    
        num = input('digite um numero: ')
        if num.isdigit():
            num = int(num)
            matriz[l].append(num)

            c+=1
        else:
            c = c
            print('digite um numero válido')
    l+=1
    c = 0
print('-='*30)
print('\n a matriz é completa é \n')
for l in range(0,4):
    for c in range(0,4):
        print(f'{matriz[l][c]}', end =' ')
    print()

print('-='*30)
print(f' e ela possui {matriz_maior_que_10(matriz)} numeros maiores que 10')