def impressao_vetor(vetor):
    return vetor

def impressao_vetor_reversa(vetor):
    return vetor[::-1]

def media_vetor(vetor):
    media = sum(vetor) / len(vetor)
    return media

quantidade = 0 
cont = 0
num = 0.0 
vetor = []

quantidade = input('digite a quantidade de numeros que você deseja adicionar na lista')
if quantidade.isdigit() and int(quantidade)> 0 :
    
    quantidade = int(quantidade)
    while cont < quantidade:
        num = input('digite um numero real: ')
        if num.replace('.','', 1).replace('-','').isdigit():
            num = int(num)
            vetor.append(num)
            cont += 1 
        else:
            cont = cont
            print('digite um numero válido')
    
    print(f' o vetor é {impressao_vetor(vetor)}')
    print(f' na ordem inversa é {impressao_vetor_reversa(vetor)}')
    print(f' e a média é  {media_vetor(vetor)}')

else:
    print('digite uma quantidade válida')
