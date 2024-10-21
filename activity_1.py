size = input("Size of Pizza (S/M/L)? : ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small size of pizza is 100 Rs.")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium size of pizza is 200 Rs.")
else:
    bill += 500
    print("Large size of pizza is 500 Rs.")

addPeperoni = input("Do you want to peperoni (Y/N) ")
if addPeperoni == 'Y' or addPeperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50

extraCheese = input("Do you want to extra cheese (Y/N)")
if extraCheese == 'Y' or extraCheese == 'y':
    bill += 20

print(f"Your final bill is {bill}")
