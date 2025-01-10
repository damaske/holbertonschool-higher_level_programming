#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
printed = f"Last digit of {number} is {last_dig}"
if last_dig > 5:
    print(f"{printed} and is greater than 5")
elif last_dig == 0:
    print(f"{printed} and is 0")
else:
    print(f"{printed} and is less than 6 and not 0")
