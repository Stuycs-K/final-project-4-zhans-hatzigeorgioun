import sys
msg = input("Enter the message you want to encrypt: ")
key1 = input("Enter your first encryption key: ")
key2 = input("Enter your second encryption key: ")
def splitter (msg):
    tbEncrypt = msg.replace(" ", "")
    if(len(tbEncrypt)%2 != 0):
    	tbEncrypt += "Q"
    splitted = ([(tbEncrypt[i:i+2]) for i in range(0, len(tbEncrypt), 2)])
    return splitted

print(splitter(msg))

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

generate_key_square(key1)
generate_key_square(key2)
#print out the key to show whats happening
print(generate_key_square(key1))
print(generate_key_square(key2))

table = ['A', 'B', 'C', 'D', 'E',
         'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O',
         'P', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']