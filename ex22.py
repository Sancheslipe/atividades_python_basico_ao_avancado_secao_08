def quantidade_linha(num):
    
    for l in range(1, num +1):
        for c in range(1, l +1):
            print('!', end ='')

        print()
    
num = int(input('digite um numero: '))
quantidade_linha(num)