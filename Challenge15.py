money = 100
currentMeal = 12
meals = []
people = 0

while True:
    money  -= currentMeal
    meals.append(currentMeal)
    currentMeal = round(currentMeal*0.95,2)
    people += 1
    if (money - currentMeal) <= 0:
        break

print(f"Guests: {people}\nLast Meal Cost: {meals[-1]}\nAverage Meal Cost: {round(sum(meals)/len(meals),2)}")