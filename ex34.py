def fatorial_duplo(num):
    cont = int(num)
    fatorialDuplo = 1
    
    for c in range(0,cont+1):
        if c % 2 != 0:
            fatorialDuplo *= c * 1
    
    return fatorialDuplo

num = input('digite um numero inteiro positivo e impar: ')
if (num.isdigit()) and (int(num) % 2 != 0):
    num = int(num)
    print(fatorial_duplo(num))
else:
    print('digite um numero válido!')
