while True:
    size = input("Enter the size of your Tree: ")
    if size.isnumeric():
        size = int(size)
        break
    else:
        print("Please enter a valid number")

fill = size*2 + 1
for n in range(size):
    n = n*2 +1
    #if n%2 != 0:
    string = "*"*n
    print(string.center(fill, " "))

print("*".center(fill, " "))
print("*".center(fill, " "))