def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        position = alphabet.index(char)
        if char in alphabet:

            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"the {cipher_direction} text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


from art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("type 'yes' if you want to continue and 'no' if you want to exit.")
    if result == 'no':
        should_continue = False
        print("goodbye!")

# def encrypt(message, shift_amt):
#     cipher_text = ""
#     for letter in message:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encoded message is {cipher_text}")



# def decrypt(message, shift_amt):
#     plain_text = ""
#     for letter in message:
#         position = alphabet.index(letter)
#         old_position = position - shift_amt
#         old_letter = alphabet[old_position]
#         plain_text += old_letter
#     print(f"the decoded message is {plain_text}")



# if direction == "encode":
#     encrypt(message=text, shift_amt=shift)
# elif direction == "decode":
#     decrypt(message=text, shift_amt=shift)
# else:
#     print("enter a valid operation.")