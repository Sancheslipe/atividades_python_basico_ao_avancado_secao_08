def consumo_litro(distancia,litros):
    calculo = distancia / litros

    if calculo < 8:
        return print('Venda o carro!')
    elif (calculo >=8 and calculo <= 12):
        return print('Econômico!')
    elif calculo > 12:
        return print('Super econômico!')

kilometros  = input('digite a distancia em kilometros: ')
if kilometros.replace('.','', 1).isdigit():
    kilometros = float(kilometros)
    
    litro = input('digite quantos litros de gasolina foram gastos: ')
    if litro.replace('.','', 1).isdigit():
        litro = float(litro)
        
        consumo_litro(kilometros, litro)
    else:
        print('digite uma litragem válida')
else:
    print('digite uma distância válida')