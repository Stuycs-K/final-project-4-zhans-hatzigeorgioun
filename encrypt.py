import sys
tbEncrypt = "ORANGEE"
if(len(tbEncrypt)%2 != 0):
	tbEncrypt += "Q"
print([(tbEncrypt[i:i+2]) for i in range(0, len(tbEncrypt), 2)])
