#Christopher Kenny
#CS 175
#Q: Write a Python program using recursion to calculate the sum of all numbers from 1 to n.

def calculate_sum(n):
  if n == 0:
    return 0
  else:
    return n + calculate_sum(n-1)

print(f"The sum of numbers is: {calculate_sum(4)}")
