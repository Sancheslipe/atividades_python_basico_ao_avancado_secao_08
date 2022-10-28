def soma_matrizA44(matriz):
    soma = 0
    for l in range(0,4):
        soma += sum(matriz[l])
    
    return soma

A = [[],[],[],[]]
num = 0 
l = 0
c = 0 
soma = 0
while l <4:
    while c < 4:
        num = input('digite  um numero: ')
        if num.isdigit():
            num = int(num)
            A[l].append(num)
            c +=1
        else:
            c = c 
            print('digite um numero válido')
    l +=1
    c = 0

soma = soma_matrizA44(A)

print(f'a soma é {soma}')