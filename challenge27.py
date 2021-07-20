# The List

list = ["Mexico", "Disney World", "Universal Studios"]

# 5 Possible options

print("1: Add a travel destination")
print("2: Find a travel destination")
print("3: Remove a travel destination")
print("4: Sort destinations alphabetically")
print("5: # of total destinations")

userC = int(input("Choose what you want to do: "))

# If they choose something that isn't an option

if userC <= 0:
    print("Your number must be larger than 0.")
    exit()

elif userC >= 6:
    print("Your number must be under 5")
    exit()

# Option #1

if userC == 1:
    UserAdd = str(input("What travel destination would you like to add: "))
    list.append(UserAdd)
    print(list)
# Option #2

if userC == 2:
    userFind = str(input("Which travel destination would you like to search for: "))
    print(list.index(userFind))


# Option #3

if userC == 3:
    UserRemove = str(input("Which travel destination would you like to remove: "))
    list.remove(UserRemove)
    print(list)
# Option #4

if userC == 4:
    print(list.sort())

# Option #5

if userC == 5:
    print(len(list))
