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

def find_position(square, letter):
    for row in range(5):
        for col in range(5):
            if square[row][col] == letter:
                return row, col

def four_square_encrypt(message, key_square1, key_square2):
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

        cipher_text += key_square2[row1][col2]
        cipher_text += key_square1[row2][col1]

    return cipher_text

key_square1 = generate_key_square(key1)
key_square2 = generate_key_square(key2)

# Print out the key squares to show what's happening
print(key_square1)
print(key_square2)

encrypted = four_square_encrypt(message, key_square1, key_square2)
print(encrypted)
