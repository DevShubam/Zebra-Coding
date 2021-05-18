word1 = str(input("Whats your first word? "))
word2 = str(input("Whats your second word? "))

word1u = word1.upper()
word1l = word1.lower()

word2u = word2.upper()
word2l = word2.lower()

print("Word one and two added together:", str(word1 + word2))
print("Word one three times:", str(word1 * 3))
print("Word two three times:", str(word2 * 3))
print("Words added together in uppercase:", str(word1u + word2u))
print("Words added together 5 times, and in lowercase", str(word1l + word2l * 5))
print("The charecter at the 3rd index for both words:", str(word1[3] + word2[3]))
print("The words sliced from index 3 to 9", str(word1[3:9] + word2[3:9]))

