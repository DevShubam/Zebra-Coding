# Starting If / Elif / Else statements :)

users_password = str(input("Enter your password here. It must contain an 'e': "))

found = users_password.find("e")

if (found == -1):
    print("Invalid")

else:
    print("Has e")
