import random
correct_guess = random.randint(0, 99)
amount_of_guesses = 0
print("Higher Lower Game")
while True:
    player_guess = int(input("Guess a number bewtween 0 and 99: "))
    if player_guess < correct_guess:
        print("Higher")
        amount_of_guesses += 1
        
    elif player_guess > correct_guess:
        print("Lower")
        amount_of_guesses += 1
        
    else:
        print("Correct guess")
        amount_of_guesses += 1
        print("Amount of guesses =", amount_of_guesses)
        break