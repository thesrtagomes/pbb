baseRetangulo =(float(input('Qual a base do retângulo? ')))
alturaRetangulo = (float(input('Qual a altura do retângulo? ')))
area = baseRetangulo * alturaRetangulo
perímetro = (2 * baseRetangulo) + (2 * alturaRetangulo)
import math
diagonal = math.sqrt(baseRetangulo**2 + alturaRetangulo**2)
print(f'A área é: {area:.0f}')
print(f'O perímetro é:  {perímetro:.0f}')
print(f'A diagonal é:  {diagonal:.2f}')