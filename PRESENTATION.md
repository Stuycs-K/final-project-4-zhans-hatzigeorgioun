# Four-Square Cipher Presentation

The Four-Square Cipher uses four grids. Each grid is a 5x5 matrix. Two of the matrices contain the alphabet with "i" and "j" combined to form 25 letters. The two other matrices also contain 25 letters, but the letters do not have to be in order. Each letter can only appear once in the matrices.

To encrypt a message using this cipher, the default keys (the matrices containing the alphabet in order) are placed in the upper left and lower right corner. The first custom key would be placed in the upper right corner and the second custom key would be placed in the lower left corner. For example, lets say our first key is `zgptfoihmuwdrcnykeqaxvsbl` and our second key is `mfnbdcrhsaxyogvituewlqzkp`. We would display the matrices like this.

Upper Left Key|Upper Right Key
|-------------------------|-------------------------|
['A', 'B', 'C', 'D', 'E'] | ['Z', 'G', 'P', 'T', 'F']
['F', 'G', 'H', 'I', 'K'] | ['O', 'I', 'H', 'M', 'U']
['L', 'M', 'N', 'O', 'P'] | ['W', 'D', 'R', 'C', 'N']
['Q', 'R', 'S', 'T', 'U'] | ['Y', 'K', 'E', 'Q', 'A']
['V', 'W', 'X', 'Y', 'Z'] | ['X', 'V', 'S', 'B', 'L']

Lower Left Key | Lower Right Key
|-------------------------|-------------------------|
['M', 'F', 'N', 'B', 'D'] | ['A', 'B', 'C', 'D', 'E']
['C', 'R', 'H', 'S', 'A'] | ['F', 'G', 'H', 'I', 'K']
['X', 'Y', 'O', 'G', 'V'] | ['L', 'M', 'N', 'O', 'P']
['I', 'T', 'U', 'E', 'W'] | ['Q', 'R', 'S', 'T', 'U']
['L', 'Q', 'Z', 'K', 'P'] | ['V', 'W', 'X', 'Y', 'Z']

Now that we have all 4 matrices in place, we can start encrypting our message. Let's say the message we want to encrypt is `ATTACK AT DAWN!` The first thing we want to do is remove all spaces and punctuation which would result in `ATTACKATDAWN`. Now, we want to pair up the letters in pairs of 2. `ATTACKATDAWN` would become `AT|TA|CK|AT|DA|WN`. We would take the first pair of letters and locate each corresponding letter in our default keys (the upper left and lower left keys). We find `A` in the upper left key and `T` in the lower right key. Now, we form a square using the letters and find the letters in the opposite corners. The letters in the opposite corners would be the first two letters in our encrypted message, which in this case would be `TI`. We would then take the next pair of letters and repeat the process until the message is fully encrypted. Below is a visualization of how you would encrypt the pair `AT`. `A` and `T` are bolded and the encrypted letters `T` and `I` are italicized.

Upper Left Key|Upper Right Key
|-------------------------|-------------------------|
[**'A'**, 'B', 'C', 'D', 'E'] | ['Z', 'G', 'P', *'T'*, 'F']
['F', 'G', 'H', 'I', 'K'] | ['O', 'I', 'H', 'M', 'U']
['L', 'M', 'N', 'O', 'P'] | ['W', 'D', 'R', 'C', 'N']
['Q', 'R', 'S', 'T', 'U'] | ['Y', 'K', 'E', 'Q', 'A']
['V', 'W', 'X', 'Y', 'Z'] | ['X', 'V', 'S', 'B', 'L']

Lower Left Key | Lower Right Key
|-------------------------|-------------------------|
['M', 'F', 'N', 'B', 'D'] | ['A', 'B', 'C', 'D', 'E']
['C', 'R', 'H', 'S', 'A'] | ['F', 'G', 'H', 'I', 'K']
['X', 'Y', 'O', 'G', 'V'] | ['L', 'M', 'N', 'O', 'P']
[*'I'*, 'T', 'U', 'E', 'W'] | ['Q', 'R', 'S', **'T'**, 'U']
['L', 'Q', 'Z', 'K', 'P'] | ['V', 'W', 'X', 'Y', 'Z']

Now, you may have noticed that `ATTACKATDAWN` pairs up evenly since it contains an even number of characters. How would we deal with an odd number of characters? We would add a letter to the end of the plaintext message. In this case, we chose the letter `Q`. So `ATTACKSATDAWN` would become `AT|TA|CK|SA|TD|AW|NQ` and we would encode our message using these pairs. When decoding, the plaintext message would become `ATTACKSATDAWNQ`

You may also have noticed that our default keys don't contain the letter `J` and might wonder how we would deal with a word that contains that letter such as `JACK`. In our default keys, `I` and `J` are combined to form the 25 letter matrix. Thus, when our code detects that the message contains the letter `J`, it would substitute it with an `I` instead and encode it. When decoding, the result would be `IACK`, but you can infer that the plaintext message is `JACK` through substitution.

The Four-Square Cipher is similar to the Playfair Cipher.