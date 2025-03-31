import sys
import datetime

name = input("What is your name? ")
age = input("How old are you? ")
now = datetime.datetime.now()
future = now.year + (100 - int(age))

print(name)
print(age)
print("You will be 100 in " + str(future))