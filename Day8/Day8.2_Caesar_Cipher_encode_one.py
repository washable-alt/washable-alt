alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

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

#Todo-3:
#Call the encrypt function and pass in the user inputs. Try encrypting a message.
cipher_text = encrypt(text, shift)

print(f"The encoded text is {cipher_text}")