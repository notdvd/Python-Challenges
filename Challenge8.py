while True:
    num = input("Enter a number: ")
    if num.isnumeric():
        break
    else:
        print("Please enter a valid number")

numbers = list(map(int,num))
sum = 0
for num in numbers:
    sum += num

print(sum)