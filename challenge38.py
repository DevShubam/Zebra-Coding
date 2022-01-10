user_str = str(input("What's your string: "))
user_inc = int(input("How much do you want to increment by: "))

if user_inc > 25:
    print("You cannot increment by a number larger than 25.")

elif user_inc <= 0:
    print("You cannot increment by a number lower than 1.")

else: 
    final_str = ""
    for letter in user_str:
        new_str = ord(letter)
        enc_str = new_str + user_inc
        if enc_str > 122:
            enc_str -= 26      
        
        if letter in [',', '.', ' ', '?']:            
            final_str += letter
        else:
            final_str += chr(enc_str)               
    print(final_str)
