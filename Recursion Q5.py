#Christopher Kenny
#CS 175
#Q: Adjust the following code

def fibonacci(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    #|***THIS IS THE ERROR**** |
    #|return fibonacci(n-1) + n|
    return fibonacci(n-1) + fibonacci(n-2) #Fixed

fibonacci(8)
