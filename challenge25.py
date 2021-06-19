import random

random_num = random.randint(1,5)

print(random_num)

userNum = str(input("What's your number? "))


if userNum == random_num:
    print("Congrats, you picked the right number.")
else:
    print("You guessed the wrong number, better luck next time")
