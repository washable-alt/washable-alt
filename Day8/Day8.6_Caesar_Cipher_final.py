from Day8_Caesar_Cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']

def print_output(direction):
    if direction == 'encode':
        cipher_text = encrypt(text, shift)
        print(f"The encoded text is {cipher_text}")
    elif direction == 'decode':
        decrypted_code = decrypt(text, shift)
        print(f"The encoded text is {decrypted_code}")

#Encrypt method

def encrypt(text, shift):
    # Todo-2: Inside the encrypt function: shift each letter of 'text' forwards in the alphabet 
    # by shift amount and print the encrypted text
    #e.g.
    #plaintext="hello"
    #shift=5
    #cipher_text="mjqqt"
    #print output: "The encoded text is mjqqt"
    cipher_text = ""
    for letter in text:
        for i in range(len(alphabet)):        
            if letter == alphabet[i]:
                # the formula (i+shift) % len(alphabet) is used to handle wrapping around the alphabet
                cipher_text += alphabet[(shift+i) % len(alphabet)]
    print(cipher_text)
    return cipher_text


#Decrypt method

def decrypt(encrypted_text, shift):
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #print output: "The decoded text is hello"

    decrypted_text = ""
    for letter in encrypted_text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                decrypted_text += alphabet[(i - shift) % len(alphabet)]               
    return decrypted_text

print(logo)

should_end = False

while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while direction != 'encode' and direction != 'decode':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    print_output(direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == 'no':
        should_end = True
        print("Goodbye")
