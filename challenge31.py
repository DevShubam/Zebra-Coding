# Write a program to get input from the user, and remove all the vowels (a,e,i,o,u) from the sentence and print the result back on screen.

string = str(input("What's the sentence you want me to remove vowels from: "))
string_length = len(string)
i = 0

while(i < string_length):
    if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
        string = string.replace(string[i], ' ')

    i += 1

print(string)
