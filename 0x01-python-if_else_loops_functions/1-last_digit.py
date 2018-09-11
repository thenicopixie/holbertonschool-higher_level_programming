#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
if number < 0:
    i = number * -1
last_dig = i % 10
if last_dig > 5:
    message = "and is greater than 5"
elif last_dig == 0:
    message = "and is zero"
elif last_dig < 6:
    if last_dig != 0:
        message = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_dig, message))
