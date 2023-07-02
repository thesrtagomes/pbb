print('Trabalhando com medidas')
A = float(input('Digite a medida A: '))
B = float(input('Digite a medida B: '))
C = float(input('Digite a medida C: '))
quadrado = A **2
triângulo = (A * B) / 2
trapézio = ((A + B) * C) / 2
print(f"A área do quadrado de lados {A:.2f} é {quadrado:.4f}.")
print(f'A área do triângulo de base {A:.2f} e altura {B:.2f} é de {triângulo:.4f}.')
print(f'A área do trapézio de bases {A:.2f} e {B:.2f} é de {trapézio:.4f}.')