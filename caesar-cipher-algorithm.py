def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        # if the letter is actually a letter
        if letter in alpha:
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        #if the letter is actually a letter
        if letter in alpha:
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def main():
    print(" ******************************* ")
    print(" *** CAESAR CIPHER ALGORITHM *** ")
    print(" ******************************* ")
    message = str(input("Enter a message: "))
    key = int(input("Enter a key: "))

    # Encrypt message with a key
    encrypted = encrypt(key, message)
    print("ENCRYPTED MESSAGE: " + encrypted)
    

    # Decrypt the encrypted message with a key
    decrypted = decrypt(key, encrypted)
    print("DECRYPTED MESSAGE: " + decrypted)

if __name__ == "__main__":
    main()