#List Method

#numbers = []

#while len(numbers) < 5:
#    num = input("Enter a number: ")
#    if num.isnumeric():
#        num = int(num)
#        numbers.append(num)
#    else:
#        print("Please enter a valid number")

#print(f"Largest Number: {max(numbers)}")

#No List Method

#def testNum(num, big):
#    try:
#        if num > big:
#            return num
#        else:
#            return big
#    except:
#        return num

#numbers = 0
#big = None

#while numbers < 5:
#    num = input("Enter a number: ")
#    if num.isnumeric():
#        num = int(num)
#        big = testNum(num, big)
#        numbers += 1
#    else:
#        print("Please enter a valid number")

#print(f"Largest Number: {big}")