letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in letters:  # check if the character is in the letters list
            position = letters.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += letters[new_position]
        else:
            cipher_text += char  # append character as it is if not in the list
    print("Encrypted text:", cipher_text)
    return cipher_text

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in letters:  # check if the character is in the letters list
            position = letters.index(char)
            new_position = (position - shift_key) % 26
            plain_text += letters[new_position]
        else:
            plain_text += char  # append character as it is if not in the list
    print("Decrypted text:", plain_text)
    return plain_text

wanna_end = False
while not wanna_end:
    what_to_do = input("encrypt or decrypt: ")
    text = input("Enter text: ")
    key = int(input("Enter key: "))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=key)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=key)
    play_again = input("Play again? (yes or no): ")
    if play_again.lower() != "yes":
        wanna_end = True

# def encryption(plain_tex, shift_key):
#     for char in plain_tex:
#         cipher_text = ""
#         position = letters.index(char)
#         new_position = (position + shift_key) % 26
#         cipher_text += letters[new_position]
# def decencryption(cipher_text, shift_key):
#     for char in cipher_text:
#         plain_text = ""
#         position = letters.index(char)
#         new_position = (position - shift_key) % 26
#         plain_text += letters[new_position]
#
# wanna_end = False
# while not wanna_end:
#     what_to_do = input("encrypt or decrypt: ")
#     text = input("Enter text: ")
#     key = int(input("Ënter key: "))
#     if what_to_do == "encrypt":
#         encryption(plain_tex=text, shift_key=key)
#     elif what_to_do == "decrypt":
#         encryption(plain_tex=text, shift_key=key)
#     play_again = input("yes or no")
#     if play_again == "yes":
#         wanna_end = False
#     else:
#         wanna_end = True
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
