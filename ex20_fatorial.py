def fatorial(num):
    calc = 1

    for i in range(1, num+1):
        calc *= i*1

    return calc

num = input('digite um numero para ser o fatorial: ')
if num.isdigit():
    num = int(num)

    print(fatorial(num))

else:
    print('digite um numero válido')