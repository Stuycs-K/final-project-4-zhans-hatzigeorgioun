import sys
import string

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.strip()
    content = content.translate(str.maketrans('', '', string.punctuation))
    return content

message_input = input("Enter the message you want to encrypt (1 for keyboard input, 2 for file input): ")
if message_input == '1':
    message = input("Enter your message: ")
elif message_input == '2':
    message_file = input("Enter the path to the message text file: ")
    message = read_text_file(message_file)
else:
    print("Invalid input")
    sys.exit(1)

key1_input = input("Enter your first encryption key (1 for keyboard input, 2 for file input): ")
if key1_input == '1':
    key1 = input("Enter your first encryption key: ")
elif key1_input == '2':
    key1_file = input("Enter the path to the first encryption key text file: ")
    key1 = read_text_file(key1_file)
else:
    print("Invalid input")
    sys.exit(1)

key2_input = input("Enter your second encryption key (1 for keyboard input, 2 for file input): ")
if key2_input == '1':
    key2 = input("Enter your second encryption key: ")
elif key2_input == '2':
    key2_file = input("Enter the path to the second encryption key text file: ")
    key2 = read_text_file(key2_file)
else:
    print("Invalid input")
    sys.exit(1)

def generate_key_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    key_square = [[None] * 5 for _ in range(5)]

    used_letters = set()
    row, col = 0, 0
    for letter in key:
        if letter not in used_letters:
            key_square[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1
                if row == 5:
                    break

    for letter in alphabet:
        if letter != "J" and letter not in used_letters:
            key_square[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1
                if row == 5:
                    break

    return key_square

default_key_square = generate_key_square("")
key_square1 = generate_key_square(key1)
key_square2 = generate_key_square(key2)
upper_left = default_key_square
upper_right = key_square1
lower_left = key_square2
lower_right = default_key_square

def encrypt(message):
    message = message.upper().replace("J", "I")
    message = message.replace(" ", "")
    message = message.translate(str.maketrans('', '', string.punctuation))
    if len(message) % 2 == 1:
        message += "Q"

    cipher_text = ""
    for i in range(0, len(message), 2):
        char1 = message[i]
        char2 = message[i + 1]

        row1, col1 = find_position(upper_left, char1)
        row2, col2 = find_position(lower_right, char2)

        cipher_text += upper_right[row1][col2]
        cipher_text += lower_left[row2][col1]

    return cipher_text


def find_position(square, char):
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j] == char:
                return i, j


print("Upper Left Key")
for row in upper_left:
    print(row)
print()

print("Upper Right Key")
for row in upper_right:
    print(row)
print()

print("Lower Left Key")
for row in lower_left:
    print(row)
print()

print("Lower Right Key")
for row in lower_right:
    print(row)
print()

encrypted_message = encrypt(message)
print("Encrypted Message:", encrypted_message)
