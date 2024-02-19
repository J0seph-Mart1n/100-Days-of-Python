alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  if direction == 'encode':
    encrypted_word = ''
    for letter in text:
      if letter in alphabet:
        index = alphabet.index(letter)
        if shift>25:
          shift=shift%26
        if index+shift>25:
          new_index = index+shift-26
          encrypted_word+=alphabet[new_index]
        else:
          encrypted_word+=alphabet[index+shift]
      else:
        encrypted_word+=letter
    print(f"The encoded text is {encrypted_word}")
  elif direction == 'decode':
    decrypted_word = ''
    for letter in text:
      if letter in alphabet:
        index = alphabet.index(letter)
        if shift>25:
          shift = shift%26
        if index-shift<0:
          new_index = index-shift+26
          decrypted_word+=alphabet[new_index]
        else:
          decrypted_word+=alphabet[index-shift]
      else:
        decrypted_word+=letter
    print(f"The decoded text is {decrypted_word}")
  else:
    print('Invalid Input')

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

  caesar(direction,text,shift)
  play = input("Type 'yes' if you want to continue: ")
  if play!="yes":
    break