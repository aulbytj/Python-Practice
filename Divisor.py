# This program asks for a number and returns all the numbers between 60 that number is divisible by

list = int(input("Give me a number: "))

divisors = []
numbers = range(60)

for num in numbers:
    if num % list == 0:
        divisors.append(num)
print(divisors)