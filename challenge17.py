totalSlices = int(input("How many slices of pizza do you have? "))

totalFriends = int(input("How many friends do you have? "))

finalAnswer = totalSlices % totalFriends

print("There will be", finalAnswer,"slice(s) left over")
