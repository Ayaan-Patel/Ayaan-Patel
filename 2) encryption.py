# To use, enter a word, choose a number, and select to encrypt. It will give a cipher.
# Then re-run the program, enter the cipher, choose your previously selected key, and select decrypt.

# This program ask the user to input a message that needs to be encrypted. It then asks for a key of choice between 1 - 26 for encryption, and the same key number for decryption.

# The program defines the function encrypt with message and key inputs, using string methods to encrypt the string as well as adding the key number to each letter of the string.

# The program defines the function decrypt by using the cipher (encrypted string) and key number. All the string methods are undone, and the key number is subtracted from each letter to return the original message.


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            encrypted +=  LETTERS[num]

    return encrypted

def decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decrypted +=  LETTERS[num]

    return decrypted

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))

if __name__ == '__main__':
    main()
