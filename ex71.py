def dentro_ret(v1,v2, P):
    dentro =True

    if P[0] <= v2[0] and P[0] >= v1[0] and \
        P[1] <=v2[1] and P[1] >= v1[1]:
        dentro = True
    else:
        dentro = False

    if dentro == True:
        return 1
    else:
        return 0 
    
    

v1 = []
v2 = []
p = []

v1X = int(input('digite o digite o x do vértice 1 '))
v1.append(v1X)
v1Y = int(input('\ndigite o digite o Y do vértice 1 '))
v1.append(v1Y)


v2X = int(input('\ndigite o digite o x do vértice 2 '))
v2.append(v2X)
v2Y = int(input('\ndigite o digite o Y do vértice 2 '))
v2.append(v2Y)

pX = int(input('\ndigite o digite o x do Ponto que deseja achar '))
p.append(pX)
pY = int(input('\ndigite o digite o Y do Ponto que deseja achar '))
p.append(pY)

print(dentro_ret(v1,v2,p))
