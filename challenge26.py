import random

random_num = random.randint(1,5)


print(random_num)

print("Let's play a guessing game, I am thinking of a number that is inbetween 1 and 5, you need to guess this number correctly. "
"You have three tries to guess it")

userNum = int(input("What is your guess: "))

# To prevent guesses that are not inbetween 1 and 5

if userNum <= 0:
    print("Your number must be larger than 0.")
    exit()

elif userNum >= 6:
    print("Your number must be under 5")
    exit()

# For Guess 1

if userNum == random_num:
    print("Congrats, you picked the right number.")

elif userNum < random_num:
    print("Your guess was too small, try again")

else:
    print("Your guess was too large, try again.")

userNum = int(input("What is your guess: "))

# For guess 2

if userNum == random_num:
    print("Congrats, you picked the right number.")

elif userNum < random_num:
    print("Your guess was too small, try again")

else:
    print("Your guess was too large.")

userNum = int(input("What is your guess: "))

# Guess 3

if userNum == random_num:
    print("Congrats, you picked the right number.")

elif userNum < random_num:
    print("Your guess was too small, try again")

else:
    print("Your guess was too large.")
