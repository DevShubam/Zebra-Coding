counter = 99
while counter > 0:
    print(str(counter) + " bottles of cola on the wall, ", str(counter) + " bottles of cola.")
    print("Take one down and pass it along, ", str(counter -1) +  " bottles of cola on the wall.") 
    counter -=1

if counter == 0:
    print("No more bottles of cola on the wall, no more bottles of cola. Go to the store and buy some more.")
