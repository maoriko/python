import string, os, pathlib


# The Encryption Function
def cipher_encrypt(to_encrypt: str, key: int):
    encrypted = ""

    for c in to_encrypt:
        if c.isupper():
            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.islower():
            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new

        else:
            encrypted += c
    return encrypted


# The Decryption Function
def cipher_decrypt(decrypted_value: str, key: int):
    decrypted = ""

    for c in decrypted_value:

        if c.isupper():
            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted_value += c_og

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted_value += c_og
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted_value += c
    return decrypted_value


# to_encrypt = "Hi"
# decrypted = cipher_encrypt(to_encrypt, 2)
# print("Plain text message:\n", to_encrypt)
# print("Encrypted text:\n", decrypted)


def cipher_using_lookup(text, key, characters=string.ascii_lowercase, decrypt=False):
    if key < 0:
        print("key cannot be negative")
        return None

    n = len(characters)

    if decrypt == True:
        key = n - key
    table = str.maketrans(characters, characters[key:] + characters[:key])
    translated_text = text.translate(table)
    return translated_text


# ---------------------- Test Encryption ----------------------

# text = "HELLO WORLD! I am Encrypted!"
# encrypted = cipher_using_lookup(text, 3, string.ascii_uppercase, decrypt=False)
# print(encrypted)

# ---------------------- Test Decryption ----------------------
# Test Decryption
# text = "KHOOR ZRUOG! L am Hncrypted!"
# decrypted = cipher_using_lookup(text, 3, string.ascii_uppercase, decrypt=True)
# print(decrypted)


# Read file function
def fileCipher(fileName, outputFileName, key=3, decrypt=False):
    with open(fileName, "r") as f_in:
        with open(outputFileName, "w") as f_out:
            # iterate over each line in input file
            for line in f_in:
                # encrypt/decrypt the line
                lineNew = cipher_using_lookup(line, key, decrypt=decrypt)

                # write the new line to output file
                f_out.write(lineNew)

    print("The file {} has been translated successfully and saved to {}".format(fileName, outputFileName))


inputFile = pathlib.Path("some_text_to_encrypt.txt")

outputFile = pathlib.Path("some_text_encrypted.txt")

fileCipher(inputFile, outputFile, key=3, decrypt=False)
