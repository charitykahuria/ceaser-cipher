#encryption formula = text = (character + number of shift) % 26(no of letters in alphabet)
#decryption formula = text = (character - number of shift) % 26(no of letters in alphabet)

def encrypt(text,no_shift):
    # text = str(input('Hello!! Please write message here: \n'))
    # no_shift = int(input("please enter number of encryption steps: \n "))
    encrypted_text = ''
    
    for letter in text:
        if letter.isupper():#check if lettr uppercase
            #convert letter to unicode
            letter_unicode = ord(letter)
            #find letter position in alphabet(0-26)
            letter_index = letter_unicode - ord('A')
            #shift to the right
            new_letter_index = (letter_index+no_shift)%26
            #convert to new letter
            new_letter_unicode =new_letter_index + ord('A')
            new_letter = chr(new_letter_unicode)
            #append new letter to encrypted string
            encrypted_text = encrypted_text+new_letter
        elif letter.islower():#check if lettr lowercase
            lower_letter_index = ord(letter)- ord('a')
            new_lower_index = (lower_letter_index + no_shift)%26
            new_lower_unicode = new_lower_index + ord('a')
            new_lower_letter = chr(new_lower_unicode)
            encrypted_text = encrypted_text+new_lower_letter

        elif letter.isdigit():#if it's a number,shift its actual value 
            number_index = (int(letter) + no_shift)%10
            encrypted_text= encrypted_text + str(number_index)
        else:#if not letter or number leave it as it is
            encrypted_text= encrypted_text + letter
    # return encrypted_text

    print(f"Encrypted message => {encrypted_text}")

encrypt(text='SOS, Please get here asap.Address is 420 Amboseli Road.',no_shift=3)


def decrypt(cipher_text,no_shift):
    decrypted_text = ''

    for character in cipher_text:
        if character.isupper():
            character_index = ord(character) - ord("A")
            character_position = (character_index - no_shift)%26
            new_character_unicode = character_position + ord("A")
            new_character = chr(new_character_unicode)
            decrypted_text = decrypted_text+new_character
        elif character.islower():
            lower_char_index = ord(character) - ord("a")
            lower_char_position = (lower_char_index - no_shift)%26
            lower_char_unicode = lower_char_position + ord("a")
            lower_character = chr(lower_char_unicode)
            decrypted_text= decrypted_text+lower_character
        elif character.isdigit():
            num_char = (int(character) - no_shift)%10
            decrypted_text= decrypted_text + str(num_char)
        else:
            decrypted_text = decrypted_text + character
    print(f'Decrypted text: {decrypted_text}')

cipher_text = 'VRV, Sohdvh jhw khuh dvds.Dgguhvv lv 753 Dpervhol Urdg.'
no_shift = 3

decrypt(cipher_text,no_shift)








