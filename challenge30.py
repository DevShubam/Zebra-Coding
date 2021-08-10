# Accept a number, n, from the user and calculate the sum of all numbers between 1 and n including n.

# For example, if user gives 10 as an input, the output should be 55

n = int(input("Give me a number: "))

counter = 0
sum = 0
while counter <= n:
    sum += counter
    counter += 1
print(sum)

