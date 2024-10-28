number = int(input("Enter number: "))
total = 0
while number != 0:
    if number > 0:
        total += number
        number = int(input("Enter numbers: "))
    else:
        number = int(input("Enter numbers: "))
print(total)