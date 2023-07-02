print('Praticando Medidas!')
largura_terreno = float(input('Qual a largura do terreno? '))
Comprimento_terreno = float(input('Qual o comprimento do terreno? '))
Metro_quadrado = float(input('Qual o valor do Metro quadrado? '))
Area_terreno = largura_terreno * Comprimento_terreno
Preço_terreno = Metro_quadrado * Area_terreno
print(f'A área do terreno é: {Area_terreno:.0f}')
print(f'O preço do terreno é R$ {Preço_terreno:.2f}')