import sys
msg = "ATTACK AT DAWN"
tbEncrypt = msg.replace(" ", "")
if(len(tbEncrypt)%2 != 0):
	tbEncrypt += "Q"
splitted = ([(tbEncrypt[i:i+2]) for i in range(0, len(tbEncrypt), 2)])
print(splitted)

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

    for letter in alphabet:
        if letter != "J" and letter not in used_letters:
            key_square[row][col] = letter
            used_letters.add(letter)
            col += 1
            if col == 5:
                col = 0
                row += 1

    return key_square