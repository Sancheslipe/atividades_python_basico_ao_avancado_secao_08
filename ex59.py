def uniao(set1,set2,uniao=[]):
    uniao = set1.union(set2)
    return uniao


vetor1 = set()
vetor2 = set()
num = 0
uniaosets = 0
cont = 0
while cont< 10:
    num = input('digite um numero: ')
    if num.replace('.','', 1).replace('-','').isdigit():
        num = float(num)
        vetor1.add(num)
        cont+=1 
    else:
        cont = cont
        print('digite um numero válido')

cont = 0

while cont< 10:
    num = input('digite um numero: ')
    if num.replace('.','', 1).replace('-','').isdigit():
        num = float(num)
        vetor2.add(num)
        cont+=1 
    else:
        cont = cont
        print('digite um numero válido')

uniaosets = uniao(vetor1,vetor2)

print(vetor2)
print(vetor1)
print(uniaosets)