
def guessing_number():
    import random
    count = 0
    guess = 0
    random_number = random.randint(1, 10)

    while guess is not random_number:
        # ensures that the user enters number values only
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Enter numbers only, try again.")
            continue

        # Stores the amount of attempts
        count += 1
        if guess is random_number:
            print(f'Congratulations!!! You got it on {count} tries.')
        elif guess > random_number:
            print("You are too high.")
        else:
            print("You are too low")


guessing_number()
