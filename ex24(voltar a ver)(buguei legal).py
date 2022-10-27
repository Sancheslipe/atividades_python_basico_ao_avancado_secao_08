# def triangulo_centralizado(num):
    
#    for l in range(1, num +1):
#         for c in range(1, l +1): 
#             print('*', end =' ')
#         print() 
#    for l1 in range(num+1, 1+1, -1):
#        for c1 in range(l1+1, 3, -1):
#            print('*',end = '')
#        
#        print()  
       
    
# num = int(input('digite um numero: '))
# triangulo_centralizado(num)



triangulo = False
num = int(input('num: '))
while triangulo != True:
    for l in range(1, num +1):
        for c in range(1, l +1): 
            print('*', end =' ')
        print() 
        
    for l1 in range(num+1, 1+1, -1):
        for c1 in range(l1+1, 3, -1):
            print('*',end = ' ')
        print()  
    triangulo = True   