number = 10
guesses_left = 5

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != "q":
    if guesses_left == 0:
        print(f"Sorry! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess = input(f"{guesses_left} Guesses Left, Guess Again? (q to quit): ")
        guesses_left -= 1

if guess == "q":
    print(f"Sorry! The number was {number}.")
