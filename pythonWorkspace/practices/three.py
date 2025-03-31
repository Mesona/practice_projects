import sys

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = []

comparator = input("Choose a number: ")
for num in list:
  if num < int(comparator):
    result.append(num)

print(result)