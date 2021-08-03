# Challenge #29: Loops - Bottles of Cola

# Write a program to create lyrics for the famous song with following lines, and print on the console.

# 99 bottles of cola on the wall, 99 bottles of cola.
# Take one down and pass it along, 98 bottles of cola on the wall.

# And so..on till

# 1 bottle of cola on the wall, 1 bottle of cola.
# Take one down and pass it around, no more bottles of cola on the wall.
# No more bottles of cola on the wall, no more bottles of cola.
# Go to the store and buy some more, 99 bottles of cola on the

counter = 1;
while counter < 99:
    counter -=1
    print(str(counter) + " bottles of cola on the wall, ", str(counter) + " bottles of cola.") 
