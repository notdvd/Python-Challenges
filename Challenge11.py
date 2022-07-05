while True:
    distance = input("Enter remaining distance in miles: ")
    if distance.isnumeric():
        distance = int(distance)
        break
    else:
        print("Please enter a valid number")

while True:
    speed = input("Enter average speed in mph: ")
    if speed.isnumeric():
        speed = int(speed)
        break
    else:
        print("Please enter a valid number")

print(f"Remaining Time: {distance/speed} Hours")
