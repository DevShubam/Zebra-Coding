userNum = int(input("What's your number: "))

def fizz_buzz():
    if userNum % 3 == 0 and userNum % 5 == 0:
        print("FizzBuzz")
    elif userNum % 3 == 0:
        print("Fizz")
    elif userNum % 5 == 0:
        print("Buzz")
    else:
        print(userNum)
fizz_buzz()