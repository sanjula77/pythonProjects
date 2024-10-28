import random
import stages

world_list = ["apple", "car", "beauty", "hello"]
choose = random.choice(world_list)
display = ["_"] * len(choose)
lives = 6
Game_Over = False

print("Word to guess:", choose)

while not Game_Over:
    Guest_letter = input("Enter letter: ").lower()

    if Guest_letter in display:
        print("You've already guessed that letter.")
    elif Guest_letter in choose:
        for position in range(len(choose)):
            if choose[position] == Guest_letter:
                display[position] = Guest_letter
        print("Correct guess!")
    else:
        lives -= 1
        print(f"Incorrect guess. Lives remaining: {lives}")

    print(" ".join(display))

    print(stages.stages[lives])

    if "_" not in display:
        Game_Over = True
        print("You win the game!")
    elif lives == 0:
        Game_Over = True
        print("You lose! The word was:", choose)

# import random
# import stages
# world_list = ["apple", "car", "beauty", "hello"]
# choose = random.choice(world_list)
# display = []
# lives = 6
# for i in choose:
#     display += "_"
# print(choose)
# Game_Over = False
# while not Game_Over:
#     Guest_letter = input("Enter letter: ").lower()
#     for position in range(len(choose)):
#         letter = choose[position]
#         if Guest_letter == letter:
#             display[position] = letter
#     print(display)
#
#     if Guest_letter not in choose:
#         lives -= 1
#         if lives == 0:
#             Game_Over = True
#             input("You are loose")
#     if '_' not in display:
#         Game_Over = True
#         print("Your are win the game")
#     print(stages.stages[lives])


# import random
# world_list = ["apple", "car", "beauty", "hello"]
# choose = random.choice(world_list)
# print(choose)
# display = []
# stop = 0
# num = 0
# for i in choose:
#     display += "_"
# print(display)
# while len(choose) != stop:
#     k = 0
#     letters = input("Enter letter: ")
#     q = 1
#     for j in choose:
#         if letters == j:
#             display[k] = letters
#             q = 0
#         k = k + 1
#     if q == 1:
#         print("Loos")
#     print(display)
#     stop = stop + 1
# print("End game")
