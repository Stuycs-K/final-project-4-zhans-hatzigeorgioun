# Work Log

## Nicko

### date 5/17

Wrote out description and did some research about the cipher. Will start the actual code tomorrow

### date 5/18

watched video on the visualization of the cipher

### date 5/19

did the splitting for the encrypt method

### date 5/22

tables are ready to be used

### date 5/23

able to pull out specific values from key tables, and use their location to start decrypting

### date 24, 2023

weird stuff going on with algorithm, making a tester

### date 25, 2023

tester made and error found, will fix tomorrow though

### date 26, 2023

error fixed, decrypt done

### date 5/30

started tryhackme room and started thinking about what to put in read me

### date 6/1

finished tryhackme room and implemented a readme that explains everything about the project

## Sean

### May 17, 2023

Worked on setting up the repo, outlining presentation and homework plans. Next step is to research the cipher

### May 18, 2023

Did some research on the cipher

### May 19, 2023

Continue research, looked into case where messages contain an odd number of characters since the cipher pairs up characters before encrypting

### May 22, 2023

Wrote generate key function, added in user input for key, and displayed output of key for demonstration purposes

### May 24, 2023
Added find_position function and encrypt function, redid splitting so that spaces were accounted for in alphabet under key function, and added printing of encrypted output. Needs to be tested to make sure it works correctly.

### May 25, 2023
Found the bug with encrypt and why it wasn't working. Only taking in two key squares instead of four

### May 26, 2023
Encryption better demo print, logic is still in progress, some parts of logic have been implemented

### June 1, 2023
Fixed encrypt code, tested it. Encrypt code works!
Made it so encrypt.py can take in txt inputs as well as user inputs. Code now strips punctuation and spaces before encrypting. Tested and works!
Started work on PRESENTATION.md, finished covering encryption algorithm.

### June 5, 2023
Finished README.md and PRESENTATION.md. Formatted encrypt for presentation/demo purposes, displays locations of the 4 key squares. Reviewed and finalized TryHackMe homework. Submitted it for public release

### June 6, 2023
Update to PRESENTATION.md about cracking cipher and keys. Update to HOMEWORK.md for updated TryHackMe link.

## References and Resources

https://www.dcode.fr/four-squares-cipher
used for testing to ensure our code works as intended

https://en.wikipedia.org/wiki/Four-square_cipher
used to understand the cipher works

https://www.youtube.com/watch?v=0cPLBdBySws
visualized cipher, further clarifications

http://practicalcryptography.com/ciphers/classical-era/four-square/
great descripion of cipher

https://people.eecs.berkeley.edu/~bh/pdf/v1ch12.pdf
explains the case where a message has an odd number of characters (add a random character at the end)
