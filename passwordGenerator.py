import random
import string
letters = int(input("How meny letters you want: "))
symbol = int(input("How meny symbol you want: "))
numbers = int(input("How meny numbers you want: "))
password = []
for i in range(letters):
    password.append(random.choice(string.ascii_letters))
for i in range(symbol):
    password.append(random.choice(string.punctuation))
for i in range(numbers):
    password.append(str(random.randint(0, 9)))
random.shuffle(password)
password = ''.join(password)
print(password)