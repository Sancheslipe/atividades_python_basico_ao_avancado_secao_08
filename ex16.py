def desenha_linha(quantidade):
    return print('='*quantidade)

vezes = input('digite o numero de vezes que você quer escrever o sinal de igual na tela: ')
if vezes.isdigit():
    vezes = int(vezes)
    desenha_linha(vezes)
else:
    print('digite um numero válido')
