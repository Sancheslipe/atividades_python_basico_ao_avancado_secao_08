def triangulo(numero):


    print()
    if (numero > 0) and (numero // 1 == numero):
        for i in range(numero+1):

            # Aqui irá informar a quantidade de espaçamento que se deve dar em cada linha
            # A primeira linha sempre possue um maior espaçamento
            for j in range(numero):

                # Por exemplo: Se o valor da variável número for 6, o valor de i for 1 e o de j for 5
                # então ele irá imprimir a primeira linha, pois 1 = 6 - 5
                if i == numero-j:
                    print((" " * j) + ("*" * (2*i-1)))

    else:
        print("Número inválido")


num = int(input("Digite um número: "))
triangulo(num)