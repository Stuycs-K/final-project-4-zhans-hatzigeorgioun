import sys
msg = "ATTACK AT DAWN"
tbEncrypt = msg.replace(" ", "")
if(len(tbEncrypt)%2 != 0):
	tbEncrypt += "Q"
splitted = ([(tbEncrypt[i:i+2]) for i in range(0, len(tbEncrypt), 2)])
print(splitted)
