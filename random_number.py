import random
number = random.randint(1, 12)
print("Let's play!")
print(f"What is the magic number: ")
hint = 1
guess = int(input("What is your guess?"))
while guess != number:
    if guess < number:
         print("Hint: Higher.")
    elif guess > number:
         print("Hint: Lower.")
    guess = int(input("What is your guess?"))  
    hint = hint + 1       
print(f"Congratulations! You got it. It took you {hint} hints!")

