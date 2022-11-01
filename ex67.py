def digitar_ate_o_fim(vetor,tamanho):
    string = 0 
    for l in range(0,tamanho):
        string = input('digite  uma string do teclado: ')
        vetor.append(string)
    
    return vetor

vetor = []
num = input(' digite o tamnho do vetor: ')
if num.isdigit():
    num = int(num)
else:
    print('digite um numero válido!')

vetor = digitar_ate_o_fim(vetor,num)
print(f'o vetor é {vetor}')