


def soma_1_ate_n(num):
    soma = 0
    cont = int(num)
    for i in range(1, num+1):
        soma += i

    return soma

num = input('digite um numero: ')
if num.isdigit() and int(num) > 0:
    num = int(num)
    print(soma_1_ate_n(num))
else:
    print('digite um numero válido')
