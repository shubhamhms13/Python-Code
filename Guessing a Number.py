secret_number = 21
no_of_guesses = 1
print("You have to guess a secret number. You have only 5 guesses.")
while no_of_guesses <= 5:
    guess_number = int(input("Guess the secret number: "))
    if guess_number > secret_number:
        print("Number is greater than secret number.\n")
    elif guess_number < secret_number:
        print("Number is lesser than secret number.\n")
    else:
        print("You won")
        print("You took",no_of_guesses,"guess to win this game.")
        break

    print((5-no_of_guesses),"guesses left.")
    no_of_guesses = no_of_guesses + 1
else:
    print("Game over...")
