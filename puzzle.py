print("Welcome to the word guessing game. Let's play!")
print("")
name = str(input("Player, what is your name? "))
word = "Bountiful"
word_guess= str(input("What is your guess?"))
times = 1
while word_guess.capitalize() != "Bountiful":
    print(f"We are very sorry, the word {word} is not the right one.")
    word_guess = str(input("What is your guess?"))
    times = times + 1

for letter in word:
    if letter.lower() == word_guess.lower():
        print(letter.upper(), end="")
    else:
        print("_", end="")

print(f"\nCongratulations {name.title()}! the word {word.capitalize()} is the correct answer! You guessed it!")
print("")
print(f"It took you {times} guesses.")