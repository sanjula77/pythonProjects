height = input("Enter ages: ")
height_list = height.split()
count = 0
for height in height_list:
    count = count + 1
for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for person in height_list:
    total = total + person

average = total / count
print(f"Average is : {average}")
