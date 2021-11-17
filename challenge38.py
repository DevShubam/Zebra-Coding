user_str = str(input("What's your string: "))
user_inc = int(input("How much do you want to increment by: "))

for letter in user_str:
    new_str = ord(letter)
    enc_str = new_str + user_inc
    final_str = chr(enc_str)
    print(final_str, end='')
