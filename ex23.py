def triangulo_vertical(num):
    
    for l in range(1, num +1):
        for c in range(1, l +1):
            print('*', end ='')
            
        print()
    for l1 in range(num+1, 1+1, -1):
        for c1 in range(l1+1, 3, -1):
            print('*',end = '')
        
        print()
    
num = int(input('digite um numero: '))
triangulo_vertical(num)