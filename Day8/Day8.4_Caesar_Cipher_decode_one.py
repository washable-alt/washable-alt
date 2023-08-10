alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

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

decrypted_text = decrypt(text, shift)

print(f"The decoded text is {decrypted_text}")