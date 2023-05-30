import sys
#msg = input("Enter the cipher text you want to decrypt: ")
#key1 = input("Enter your first encryption key: ")
#key2 = input("Enter your second encryption key: ")

msg = "TIYBFHTIZBSY"
key1 = "zgptfoihmuwdrcnykeqaxvsbl"
key2 = "mfnbdcrhsaxyogvituewlqzkp"
table = [['A', 'B', 'C', 'D', 'E'],
         ['F', 'G', 'H', 'I', 'K'],
         ['L', 'M', 'N', 'O', 'P'],
         ['Q', 'R', 'S', 'T', 'U'],
         ['V', 'W', 'X', 'Y', 'Z']]

def splitter (msg):
    tbEncrypt = msg.replace(" ", "").upper()
    if(len(tbEncrypt)%2 != 0):
    	tbEncrypt += "Q"
    splitted = ([(tbEncrypt[i:i+2]) for i in range(0, len(tbEncrypt), 2)])
    return splitted
dec = splitter(msg)

def generate_key_square(key):
    alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
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

encryptedT1 = generate_key_square(key1)
encryptedT2 = generate_key_square(key2)

key1 = key1.upper()
key2 = key2.upper()
answerXi = 0
answerXj = 0
answerYi = 0
answerYj = 0
final = ""
for p in range(len(dec)):
    char1 = dec[p][0]
    char2 = dec[p][1]
    for i in range(len(encryptedT1)):
        for j in range(len(encryptedT1[i])):
            if(encryptedT1[i][j] == char1):
                answerXi = i
                answerXj = j
    for i in range(len(encryptedT2)):
        for j in range(len(encryptedT2[i])):
            if(encryptedT2[i][j] == char2):
                answerYi = i
                answerYj = j
    #print(str(answerYi) + " " + str(answerYj))

    #print(table[0][2])
    #print(table[1][4])
    #print(table[answerXi][answerYj])
    #print(table[answerXj][answerYi])
    final += table[answerXi][answerYj]
    final += table[answerYi][answerXj]
print(final)

#print out the key to show whats happening
#print(encryptedT1)
#print(encryptedT2)
