duração = int(input('Digite a duração em segundos: '))
horas = duração // 3600
resto = duração % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}: {minutos}: {segundos}")