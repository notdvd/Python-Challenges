current = 0
total = 0

while current <= 100:
    if current%4 == 0:
        print(f"{current} ignored!")
    else:
        total += current
    current += 1

print(total)
