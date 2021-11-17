# We are going to create a hangman like program. Make sure you test every step properly before you move on to the next one.

# Make a list to store 10 words. - Done
# Pick a random word from the list and save it somewhere - Done
# Print the length of the random word - Done
# Give players 5 chances to guess the letters in the word while giving them appropriate success and failure messages. - Done
# On the 6th attempt, ask them to guess the whole word. Compare the randomly selected word with the user’s guess, if it is correct, the user wins. -

# Hint: you can use if i in word - to check if a particular letter is in the word. 


import random
wordS = ["dog", "cat", "fish", "giraffe", "lion", "spider", "zebra", "elephant", "shark", "turtle"] 

word = random.choice(wordS)

print("The word has this many letters:", len(word))
print("Here is the word:", word)

for i in range(1, 6):
    print("Guess",i)
    userguess = input("Guess your letter: ")
    # If it's correct
    if userguess in word:
        print("Correct")
    # If it's not correct
    else:
        print("Incorrect")

final_guess = str(input("Final Guess: Guess the whole word: "))

if final_guess == word:
        print("Congratulations, you got it")
else:
    print("Unfortunately, you were not correct.")
