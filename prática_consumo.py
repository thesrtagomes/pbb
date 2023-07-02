print('Qual o cunsumo médio por litro?')
distancia = float(input('Qual a distância percorrida? '))
combustível = float(input('Quanto combustível foi gasto? '))
consumoMedio = distancia / combustível
print(f'O consumo médio é de {consumoMedio:.3f} km por litro de combustível utilizado.')