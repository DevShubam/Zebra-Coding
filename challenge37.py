# Encryption, makes each chareceter increment by 1

user_str = str(input("What's your string: "))

for letter in user_str:
    new_str = ord(letter)
    enc_str = new_str + 1
    final_str = chr(enc_str)
    print(final_str, end='')
