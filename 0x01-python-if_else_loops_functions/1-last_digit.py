#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    remainder = (abs(number) % 10) * -1
else:
    remainder = number % 10

string = f"Last digit of {number} is {remainder}"

if remainder > 5:
    print(f"{string} and is greater than 5")
elif remainder == 0:
    print(f"{string} and is 0")
elif remainder < 6 and remainder != 0:
    print(f"{string} and is less than 6 and not 0")
