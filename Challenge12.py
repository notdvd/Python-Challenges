from datetime import *

dob = input("Enter date of birth in DD-MM-YYYY format: ")
dob = dob.split("-")
day = int(dob[0])
month = int(dob[1])
year = int(dob[2])
currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
today = date(currentYear, currentMonth, currentDay)

if month > currentMonth:
    diff = date(currentYear, month, day) - today
else:
    diff = date(currentYear+1, month, day) - today

print(f"Sleeps until birthday: {diff}")


