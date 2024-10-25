# total = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         total = total + i
# print(total)

end = int(input("Enter end number: "))
for i in range(1, end):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


