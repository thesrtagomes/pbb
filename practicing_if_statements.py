print("Which number is the greater?")
number_1 = float(input("Please insert the first number here: "))
number_2 = float(input("Please insert the second number here: "))
if number_1 > number_2:
    print("Number 1 is greater than number 2!")
else:
    print("Number 1 is not greater than number 2.")
if number_1 == number_2:
    print("Number 1 and number 2 are equal!")
else:
    print("Number 1 and number 2 are not equal. ")  
if number_2 > number_1:
    print("Number 2 is greater than number 1.") 
else:
    print("Number 2 is not greater than number 1.")  
print("")
print("")
animal = str(input("Write here your favorite animal: "))
if animal.lower() == "dog":
    print("That is my favorite animal too!")
else:
    print("That one is not my favorite animal. I am sorry.")

