def soma(v1,v2,res):
    somas = 0
    for x in range(0,3):
        somas = v1[x] + v2[x]
        res.append(somas)
    
    return res
v1 = []
v2 = []
result = []
x1 = 0
x2 = 0
y1 = 0
y2 = 0
z1 = 0
z2 = 0

x1 = input('digite um numero referente ao X do v1: ')
if x1.replace('.','', 1).isdigit():

    x1 = float(x1)
    y1 = input('digite um numero referente ao Y do v1: ')
    if y1.replace('.','', 1).isdigit():
        y1 = float(y1)
        z1 = input('digite um numero referente ao Z do V1: ')
        if z1.replace('.','', 1).isdigit():
            z1 = float(z1)
            
            v1.append(x1)
            v1.append(y1)
            v1.append(z1)


        else:
            print('digite um numero válido')
    else:
        print('digite um numero válido')
else:
    print('digite um numero válido')

x2 = input('digite um numero referente ao X do v2: ')
if x2.replace('.','', 1).isdigit():

    x2 = float(x2)
    y2 = input('digite um numero referente ao Y do v2: ')
    if y2.replace('.','', 1).isdigit():
        y2 = float(y2)
        z2 = input('digite um numero referente ao Z do V2: ')
        if z2.replace('.','', 1).isdigit():
            z2 = float(z2)
            
            v2.append(x2)
            v2.append(y2)
            v2.append(z2)


        else:
            print('digite um numero válido')
    else:
        print('digite um numero válido')
else:
    print('digite um numero válido')

print(soma(v1,v2,result))