import sys

message = input("Enter the message you want to encrypt: ")
key1 = input("Enter your first encryption key: ")
key2 = input("Enter your second encryption key: ")

default_key_square = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z'],
]

def generate_key_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ "
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

def find_position(square, letter):
    for row in range(5):
        for col in range(5):
            if square[row][col] == letter:
                return row, col

def four_square_encrypt(message, key_square1, key_square2, key_square3, key_square4):
    message = message.upper().replace("J", "I")
    cipher_text = ""
    for i in range(0, len(message), 2):
        letter1 = message[i]
        letter2 = message[i + 1] if i + 1 < len(message) else "X"

        if letter1 == " ":
            cipher_text += " "
            continue

        if letter2 == " ":
            cipher_text += " "
            continue

        row1, col1 = find_position(key_square1, letter1)
        row2, col2 = find_position(key_square2, letter2)

        cipher_text += key_square4[row1][col2]
        cipher_text += key_square3[row2][col1]

    return cipher_text

key_square1 = generate_key_square(key1)
key_square2 = generate_key_square(key2)

# Rearrange the key squares into their respective quadrants
key_square_upper_left = default_key_square
key_square_upper_right = key_square1
key_square_lower_left = key_square2
key_square_lower_right = default_key_square

# Print out the key squares to show what's happening
print("Default Key Square Upper Left Quadrant):")
for row in key_square_upper_left:
    print(row)
print()

print("First Key Square (Upper Right Quadrant):")
for row in key_square_upper_right:
    print(row)
print()

print("Second Key Square (Lower Left Quadrant):")
for row in key_square_lower_left:
    print(row)
print()

print("Default Key Square Lower Right Quadrant):")
for row in key_square_lower_right:
    print(row)
print()

# Encrypt the message using the rearranged key squares
encrypted = four_square_encrypt(message, key_square_upper_left, key_square_upper_right, key_square_lower_left, key_square_lower_right)
print("Encrypted message:", encrypted)
