# Create a program that manages a grocery list for the user:

# Add grocery item
#    - Input - item to add
#    - Output - sorted list
# Print grocery list
#    - Input - none
#    - Output - grocery list printed
# Sort grocery items
#    - Input - none
#    - Output - sorted list
# Remove grocery item
#    - Input- item to remove
#    - Output - new list
# Count groceries
#    - Input - none
#    - Output - number of items in list
# Replace grocery item
#    - Input - item to be replace
#    - Input - new item to replace with
#    - Output - new list
# Do as description states for all menu items. You can have a default list to start off with.
#######################################################################################################

# The default list

list = ["item1", "item2"]

# Options

print("1: Add Grocery Item")
print("2: Print the grocery list")
print("3: Print sorted list")
print("4: Remove Grocery Item")
print("5: # of total grocieries")
print("6: Replace a grocery item")

userChoice = int(input("Choose what you want to do: "))

# If they choose something that isn't an option

if userChoice <= 0:
    print("Your number must be larger than 0.")
    exit()

elif userChoice >= 7:
    print("Your number must be under 5")
    exit()

# Option 1

if userChoice == 1:
    userAdd = str(input("What item do you want to add: "))
    list.append(userAdd)
    print(sorted(list))

# 2
if userChoice == 2:
    print(list)

# 3
if userChoice == 3:
    print(sorted(list))

# 4 
if userChoice == 4:
    userRemove = str(input("What item do you want to remove: "))
    list.remove(userRemove)
    print(list)

# 5
if userChoice == 5:
    print(len(list))

# 6
if userChoice == 6:
    replace = str(input("What item do you want to replace: "))
    list.remove(replace)
    list_replaced = str(input("What Item do you want to replace it with: "))
    list.append(list_replaced)
    print(list)
