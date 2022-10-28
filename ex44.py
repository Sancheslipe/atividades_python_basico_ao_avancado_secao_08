def separar_impar_e_par(vetorX,vetorA,vetorB):
    vetorGeral = vetorX[:]
    for l in range(0,len(vetorGeral)):
        if vetorGeral[l] % 2 == 0:
            vetorA.append(vetorGeral[l])
        else:
            vetorB.append(vetorGeral[l])
        
    return vetorA , vetorB

vetor = list()
A = list()
B = list()
num = 0
cont = 1

while cont <=30:
    num = input('digite o numero para adicionar no vetor Geral')
    if num.isdigit():
        num = int(num)
        cont += 1
        vetor.append(num)

    else:
        cont = cont
        print('Digite um numero válido')

A,B = separar_impar_e_par(vetor,A,B)
print(f'  o vetor geral é {vetor}')
print(f' o vetor que possui os pares é {A}, o vetor que possui os impares {B}')