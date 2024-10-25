numbers = input("Enter numbers: ")
number = numbers.split()
count = 0
maxNum = int(number[0])
for numCunt in number:
    count = count + 1
for i in range(count):
    number[i] = int(number[i])
    if maxNum < number[i]:
        maxNum = number[i]
print(f"Max number is : {maxNum}")