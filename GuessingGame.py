# Guessing game..... program gives you three chances to guess the
# correct number, if successful/unsuccessful print message.

winning_number = 16
guess_count = 0
guess_limit = 3

# will continue to ask "Guess the number" for 3 times
while guess_count < guess_limit:
    ans = int(input("Guess the number "))

    # increases the value stored in guess_count by 1
    guess_count += 1
    if ans == winning_number:
        print(f"{ans} is correct")
        break
    else:
        print("Try again")
