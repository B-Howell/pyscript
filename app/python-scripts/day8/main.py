alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from cipher_art.py
from cipher_art import logo
print(logo)

should_end = False
while not should_end:

    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    direction = input("\u200b")

    print("Type your message:")
    text = input("\u200b").lower()

    print("Type the shift number:")
    shift = int(input("\u200b"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    restart = input("\u200b")
    if restart == "no":
        should_end = True
        print("Goodbye")
