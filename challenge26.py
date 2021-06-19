###############
#  Not Done   #
###############

# Extend challenge 25 to give more information to the user.

# Ask them to guess the number 3 times (we have not learned repeated loops yet so you will have the same code repeated 3 times.

# If the user’s guess is less than the actual number, tell the user “The number is less than your guess”
# If the user’s guess is greater than the actual number, tell the user “The number is greater than your guess”
# If the users guess equals the random number, tell the user “You guessed it right!”

import random

random_num = random.randint(1,5)


print(random_num)

userNum = int(input("Pick a number between 1 and 5."))

if userNum == random_num:
    print("Congrats, you picked the right number.")
