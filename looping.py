#First code
number = int(input("Please insert a number greater than 99:"))
while number < 99:
    print("I am sorry, please try again.")
    number = int(input("Please insert a number greater than 99:"))
print("Congratulations, you have chosen the right number")

#Another code here:
number = 0
while number < 10:
    print("Try again. ")
    number = int(input("What is the number? "))
print(f"The number is {number}")

#example adding a string in the if statement
number = 0
name = ""
while number < 50:
    print("Try again baby")
    number = int(input("What is the number?"))
    name = str(input("What is your name? "))
print(f"Your name is {name.capitalize()} and the number is {number:.2f}.")

#Activity
number = 0
number = int(input("Please type a positive number here: "))
while number <= 0:
    print("We are very sorry baby, please try again.")
    number = int(input("Please type a positive number here: "))
print(f"Congratulations! The number is: {number}.")

#Activity 2:
answer = "no"
while answer =="no":
    answer = str(input("May I have a piece of candy now? "))
if answer =="yes":
    print("Thank you")
else:
    print("Error. Start over.")    

    #OR it could be written like this:

answer = ""
while answer != "yes":
    answer = str(input("May I have a piece of candy now? "))
print("Thank you")
