def triangulos(lado1,lado2,lado3):
    ehTriangulo = False
    if lado1 < lado2 + lado3:
        ehTriangulo = True
    elif lado2 < lado1 + lado3:
        ehTriangulo = True
    elif lado3 < lado2 + lado1:
        ehTriangulo = True
    

    if ehTriangulo == True:
        if lado1 == lado2 == lado3:
            return print('equilatero')
        
        elif lado1 == lado2 != lado3:
            return print('isóceles')
        elif lado1 == lado3 != lado2:
            return print('isóceles')
        elif lado2 == lado3 != lado1:
            return print('isócles')

        elif lado1 != lado2 != lado3:
            return print('Escaleno')
    else:
        return print('não é um triangulo')


lado1 = input('digite o valor do lado 1: ')
if lado1.replace('.','', 1).isdigit():
    lado1= float(lado1)

    lado2 = input('digite o valor do lado 1: ')
    if lado2.replace('.','', 1).isdigit():
        lado2= float(lado2)

        lado3 = input('digite o valor do lado 1: ')
        if lado3.replace('.','', 1).isdigit():
            lado3= float(lado3)

            triangulos(lado1,lado2,lado3)

        else:
            print('digite um lado válido')
    else:
        print('digite um lado válido')
else:
    print('digite um lado válido')