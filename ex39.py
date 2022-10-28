def troque(A,B):
    troca1 = A
    troca2 = B

    A = troca2
    B = troca1

    return  A,B
C= 0
D= 0
num1 = input(' digite um numeroreal: ')
if num1.replace('.','', 1).replace('-','').isdigit():
    num1 = float(num1)
    num2 = input('digite um numero real: ')
    if num2.replace('.','', 1).replace('-','').isdigit():
        num2 = float(num2)
    
        C ,D = troque(num1,num2)
        print(f'este é o C {C}, este é o D {D}')
    else:
        print('digite um numero válido')

else:
    print('digite um numero válido')