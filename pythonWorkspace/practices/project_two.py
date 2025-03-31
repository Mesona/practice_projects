import sys

num = input("Pick a number: ")

if int(num) % 4 == 0:
  print("The number is evenly dividable by 4!")
elif int(num) % 2 == 0:
  print("The number is even!")
else:
  print("The number is odd!")