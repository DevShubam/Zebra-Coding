# Challenge #19: Strings - Username and Password

# Create a program that validates the username and password of the user.

# It should ask for input of the username and check that the username is all alphabetical - print true or false accordingly.
# It should also ask for the password of the user and check that the password is all digits - print true or false accordingly.

username = str(input("Enter your Username: "))
password = str(input("Enter your Password: "))

print(username.isalpha())
print(username.isdigit())

print(password.isdigit())
print(password.isalpha())
