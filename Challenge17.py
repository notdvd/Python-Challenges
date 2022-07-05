def getGrade():
    while True:
        grade = input("Enter a number: ")
        if grade.isnumeric():
            grade = int(grade)
            if grade >= 0 and grade <= 100:
                return str(grade)
            else:
                print("please enter a number between 0 and 100")
        else:
            print("Please enter a valid number")

#Get data
file = open("studentsFile.txt", "r")
data = file.readlines()
file.close()
print(data)

#Change Data
for l in range(0,len(data)):
    line = data[l]
    line += " "+getGrade()+"\n"
    data[l] = line
print(data)

#Add New Data
file = open("studentsFileChanged.txt", "w")
for line in data:
    file.write(line)
file.close()