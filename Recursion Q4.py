#Christopher Kenny
#CS 175
#Q: Write the base case for a function that calculates the factorial of a number using recurion

def factorial(num):
  if num == 0: #Base case
    return 1 #Base case
  else:
    return num * factorial(num-1)

factorial(4)
