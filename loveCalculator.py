"""
boyName = input("Enter boy name : ")
girlName = input("Enter girl name : ")

boy = boyName.lower()
girl = girlName.lower()

countLine_1 = 0
countLine_2 = 0

countLine_1 += boy.count('t')
countLine_1 += boy.count('r')
countLine_1 += boy.count('u')
countLine_1 += boy.count('e')
countLine_1 += girl.count('t')
countLine_1 += girl.count('r')
countLine_1 += girl.count('u')
countLine_1 += girl.count('e')

countLine_2 += girl.count('l')
countLine_2 += girl.count('o')
countLine_2 += girl.count('v')
countLine_2 += girl.count('e')
countLine_2 += boy.count('l')
countLine_2 += boy.count('o')
countLine_2 += boy.count('v')
countLine_2 += boy.count('e')

score = int(str(countLine_1) + str(countLine_2))

if score < 10 or score > 90:
    print(f"Your Love Score is {score} and you go together like cook and mentos")

elif score >= 40 and score <= 60:
    print(f"Your Love Score is {score} and you are alright together")
else:
    print(f"Your Love Score is {score}")
"""


def calculate_love_score():
    while True:
        # Input with validation
        boyName = input("Enter boy name: ").strip()
        girlName = input("Enter girl name: ").strip()

        if not boyName.isalpha() or not girlName.isalpha():
            print("Error: Please enter valid names containing only alphabetic characters.")
            continue

        boy = boyName.lower()
        girl = girlName.lower()

        # Initialize counts
        countLine_1 = 0
        countLine_2 = 0

        # Counting occurrences of letters for "TRUE"
        for char in "true":
            countLine_1 += boy.count(char)
            countLine_1 += girl.count(char)

        # Counting occurrences of letters for "LOVE"
        for char in "love":
            countLine_2 += boy.count(char)
            countLine_2 += girl.count(char)

        # Create score from counts
        score = int(f"{countLine_1}{countLine_2}")

        # Displaying results with meaningful messages
        print("\n********** Result **********")
        if score < 10 or score > 90:
            print(f"Your Love Score is {score}. You go together like Coke and Mentos! 💥")
        elif 40 <= score <= 60:
            print(f"Your Love Score is {score}. You are alright together. 😊")
        elif 20 <= score < 40:
            print(f"Your Love Score is {score}. There's potential, but it might take some work. 🌱")
        elif score < 20:
            print(f"Your Love Score is {score}. It might not be a match made in heaven. 💔")
        else:
            print(f"Your Love Score is {score}. There's definitely a spark! 🔥")
        print("****************************\n")

        # Option to try again
        retry = input("Would you like to try with different names? (yes/no): ").lower()
        if retry != 'yes':
            break


# Call the function to start the program
calculate_love_score()
