while True:
    num = input("Enter a number: ")
    if num.isnumeric():
        num = int(num)
        break
    else:
        print("Please enter a valid number")

for x in range(1,11):
    print(f"{x} x {num} = {x*num}")
