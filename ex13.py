def calculos(num1,num2, simbolo):
    calculo = 0
    if simbolo == '+':
        calculo = num1 + num2
        return calculo
    elif simbolo == '-':
        calculo = num1 - num2
        return calculo
    elif simbolo == '*':
        calculo = num1 * num2
        return calculo
    elif simbolo == '/':
        calculo = num1 / num2 
        return calculo

print(' digite [+] para fazer a soma de 2 numeros \n digite [-] para fazer a subtração de 2 numeros ')
print(' digite [*] para fazer a multiplicação de 2 numeros \n digite [/] para fazer a divisão de 2 numeros\n')

operacao = input('digite aqui a operação desejada: ')

if operacao == '+':
    n1 = input('digite o numero 1: ')
    if n1.isdigit():
        n1 = int(n1)
        n2 = input('digite o numero 2: ')
        if n2.isdigit():
            n2 = int(n2)
            print(calculos(n1,n2,operacao))
        else:
            print('digite um numero válido')
    else:
        print('digite um numero válido')
elif operacao == '-':
    n1 = input('digite o numero 1: ')
    if n1.isdigit():
        n1 = int(n1)
        n2 = input('digite o numero 2: ')
        if n2.isdigit():
            n2 = int(n2)
            print(calculos(n1,n2,operacao))
        else:
            print('digite um numero válido')
    else:
        print('digite um numero válido')
elif operacao == '*':
    n1 = input('digite o numero 1: ')
    if n1.isdigit():
        n1 = int(n1)
        n2 = input('digite o numero 2: ')
        if n2.isdigit():
            n2 = int(n2)
            print(calculos(n1,n2,operacao))
        else:
            print('digite um numero válido')
    else:
        print('digite um numero válido')
elif operacao == '/':
    n1 = input('digite o numero 1 (tem que ser maior do que zero): ')
    
    if n1.isdigit() and int(n1) > 0 :
        n1 = int(n1)
        n2 = input('digite o numero 2 (tem que ser maior que zero): ')
        if n2.isdigit()and int(n2) > 0:
            n2 = int(n2)
            print(calculos(n1,n2,operacao))
        else:
            print('digite um numero válido')
    else:
        print('digite um numero válido')
else:
    print('digite uma operação válida')