# Rewrite challenge 29, 30 and 31 using a FOR loop.

# 29

print("CHALLENGE 29: ")
print(" ")
print(" ")


for counter in reversed(range(2, 100)):
    print(counter, "bottles of cola on the wall, ", counter, "bottles of cola.")
    print("Take one down and pass it along,", counter -1, "bottles of cola on the wall.")

if counter == 2:
    print("No more bottles of cola on the wall, no more bottles of cola. Go to the store and buy some more.")

# 30
# Accept a number, n, from the user and calculate the sum of all numbers between 1 and n including n.
# For example, if user gives 10 as an input, the output should be 55
print("CHALLENGE 30:")
print(" ")
print(" ")


n = int(input("Give me a number: "))



# 31
# Write a program to get input from the user, and remove all the vowels (a,e,i,o,u) from the sentence and print the result back on screen.

print("CHALLENGE 31:")
print(" ")
print(" ")

vowelgone = str(input("Enter any string to remove all vowels from it: "))
vowels = ("aeiouyAEIOUY") # needs captial letters to remove capital i think

for x in vowelgone:
   if x in vowels:
       vowelgone = vowelgone.replace(x, "")
print(vowelgone)

