def ibge(vetor):
    vetor = [[],[],[],[],[]]
    s = 0
    corOlhos = 0
    corCabelo = 0
    id = 0
    p = 0
    q = 0

    while p < 5:
        while q <4:

            if q == 0:
                print('[F] Feminino [M] Masculino\n')
                s = input('digite o sexo: ')
                vetor[p].append(s.upper())
                q+= 1

            elif q == 1:
                print('[A] Azuis  [C] Castanhos \n')
                corOlhos = input('digite a cor de seus olhos: ')
                vetor[p].append(corOlhos.upper())
                q+= 1

            elif q == 2:
                print('[L] Louros [P] Pretos [C] Castanhos \n')
                corCabelo = input('digite a cor de seus Cabelos: ')
                vetor[p].append(corCabelo.upper())
                q+= 1

            elif q == 3:
                idade = input('digite a sua idade: ')
                if idade.isdigit():
                    idade = int(idade)
                    vetor[p].append(idade)
                    q+= 1
                else:
                    print('digite uma idade válida')
                    q = q 
        p += 1 
        q = 0
    return vetor

def media_olhos_castanhos_cabelos_pretos(vetor):
    SomaOlhosCastanhos = 0
    media = 0 
    cont1 = 0
    for l in range(0,5):
        if vetor[l][1] == 'C' and vetor[l][2] == 'P':
            SomaOlhosCastanhos += vetor[l][3]
            cont1 +=1


        if cont1 == 0:
            return 0
        
        media = SomaOlhosCastanhos / cont1
    
    return media

def maior_idade(vetor):
    maiorIdade = 0
    for l in range(0,5):
        if vetor[l][3] > maiorIdade:
            maiorIdade = vetor[l][3]

    return maiorIdade

def loira_odonto(vetor):
    qtdeLoiraOdonto = 0
    for l in range(0,5):
        if (vetor[l][0] == 'F') and (vetor[l][1] == 'A') and \
           (vetor[l][2] == 'L') and (vetor[l][3] >= 18 and  vetor[l][3] <=35):
           
            qtdeLoiraOdonto += 1

    return qtdeLoiraOdonto

vetor = []

vetor = ibge(vetor)

print(vetor)

print('\na media dos olhos castanhos e cabelo preto é\n')
print(media_olhos_castanhos_cabelos_pretos(vetor))

print('\na maior idade é\n')
print(maior_idade(vetor))

print('\na quantidade de Mulheres entre 18 e 35 que possuem olhos azuis e cabelos loiros é\n')
print(loira_odonto(vetor))