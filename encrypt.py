import sys

message = input("Enter the message you want to encrypt: ")
key1 = input("Enter your first encryption key: ")
key2 = input("Enter your second encryption key: ")

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

#Print for demo purposes
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