letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#Definition
def encrypt_text(plain_text,shift_key,task):
    cipher_text=""#empty is stored
    if task=="d":
        shift_key=shift_key*-1
    for i in plain_text:
        if(i in letters):
            position=letters.index(i)# i takes value from variable plain_text and index() provides index no. of that value
            new_position=(position+shift_key)%26 # %26 does not allow to exeed value greater than 25
            cipher_text=cipher_text+letters[new_position]
        else:
            cipher_text=cipher_text+i
    if(task=="e"):    
        print(f"Your Encrypted text is: {cipher_text}")
    else:
        print(f"Your Decrypted text is: {cipher_text}")
#Input
wanna_end=False
while not wanna_end:
    what_to_do=input("Type 'e' for encryption and 'd' to decrypt message'")
    message=input("Type your message:\n").lower()
    shift=int(input("Enter shift key:\n"))
#Calling
    encrypt_text(plain_text=message,shift_key=shift,task=what_to_do)
    play_again=input("Enter yes to Continue and no to Exit: ")
    if (play_again=="no"):
         wanna_end=True
         print("your task is finished!!!")