#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of "
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10
if last > 5:
    print("{}{} is {} and is greater than 5".format(str, number, last))
elif last == 0:
    print("{}{} is {} and is 0".format(str, number, last))
elif last < 6 and last != 0:
    print("{}{} is {} and is less than 6 and not 0".format(str, number, last))
