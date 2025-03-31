import sys

number = input("Select a number: ")

nums = list(range(1, int(number)))
results = []

for num in nums:
  if int(number) % num == 0:
    results.append(num)

print(results)