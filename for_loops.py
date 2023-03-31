#Atividade 1
compras = ["feijão", "arroz", "massa", "carne"]
print("Lista de compras:")
for item in compras:
    print(f"comprar: {item}")

#numbers
numbers = range(15)
for number in range(15):
    print(number)

#teste com numeros
compras = [13, 2, 5, 8]
print("Numeros:")
for item in compras:
    print(f"O numero é: {item}")

 #meu teste
sabor = ["limão", "Laranja", "melancia"]
for item in sabor:
    print(f"O sabor é: {item}")

#pulando numeros:
decimal = range(0, 110, 10)
for decimal in range(0, 110, 10):
    print(decimal)

#unidade
j = range(10, 13)
i = range(5)
k = range(5, 10)
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")
        for k in range(5, 10):
            print(f"{k}--")

#letters
first_name = "Pamela"
for letter in first_name:
    print(f"The letter is: {letter}")
second_letter = first_name[1]
print(f"The second letter is: {second_letter.upper()}")

#Iterating through each letter using an index
word = "bountiful"
number_of_letters = 9
for index in range(number_of_letters):
    letter = word[index]
    print(f"index: {index} Letter: {letter}.")

#encontrar o comprimento or length
dog_name = str(input("What is your dog's name?"))
letter_count = len(dog_name)
print(f"{dog_name.title()} has {letter_count} letters.")

#outro jeito para comprimento
dogname = str(input("Dog name: "))
number_of_letter = len(dogname)
for index in range(number_of_letter):
    letter = dogname[index]
    print(f" Index: {index} and Letter: {letter}")


#Usando enumerate
my_name = str(input(" What is your name? "))
for i, letter in enumerate(my_name):
    print(f"The letter {letter.upper()} is at position {i} ")


#Activity 1
colors = ["red", "blue", "green", "yellow"]
for item in colors:
    print(item)

print()

numbers = range(1, 9)
for item in range(1, 9):
    print(item)

print()
numberstwo = range(2, 22, 2)
for number in range(2, 22, 2):
    print(number)
print()

#team activity 

word = "commitment"
favorite_letter = input("What is your favorite letter? ")
for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")

