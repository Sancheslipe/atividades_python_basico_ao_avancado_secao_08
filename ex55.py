def soma_diagonal_principal_e_secundaria(matriz):
    somaPrincipal = 0
    somaSecundaria = 0

    for l in range(0,3):
        for c in range(0,3):
            if (l == 0 and c  == 0) :
                somaPrincipal += matriz[l][c]
                
            
            elif l == 1 and c == 1:
                somaPrincipal += matriz[l][c]
                

            elif l == 2 and c == 2:
                somaPrincipal += matriz[l][c]
                

    
    for l in range(0,3):
        for c in range(0,3):
            if (l == 0 and c  == 2) :
                somaSecundaria += matriz[l][c]
                
            elif l == 1 and c == 1:
                somaSecundaria += matriz[l][c]
                
            elif l == 2 and c == 0:
                somaSecundaria += matriz[l][c]
                
    return somaPrincipal, somaSecundaria 

soma1 = 0
soma2 = 0
num = 0
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        num = int(input(' digite um numero: '))
        matriz[l].append(num) 

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}', end =' ')
    print()

soma1,soma2 = soma_diagonal_principal_e_secundaria(matriz)

print(f' a soma primaria é {soma1}, a secundaria é {soma2}')

