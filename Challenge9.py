import random

while True:
    num = input("Enter a number to be the length of your list: ")
    if num.isnumeric():
        num = int(num)
        break
    else:
        print("Please enter a valid number")

numbers = []
for n in range(1,num+1):
    numbers.append(n)
print(numbers)

for n in numbers:
    if n%5 == 0 and n%3 == 0:
        numbers[numbers.index(n)] = "FIZZ BUZZ"
    elif n%5 == 0:
        numbers[numbers.index(n)] = "FIZZ BUZZ"
    elif n%3 == 0:
        numbers[numbers.index(n)] = "FIZZ BUZZ"

print(numbers)

