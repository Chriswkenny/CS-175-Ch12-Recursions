#Christopher Kenny
#CS 175
#Q: Write a Python program to reverse a string using recursion

def reverse_string(s):
  if len(s) == 0:
    return s
  else:
    return s[-1] + reverse_string(s[:-1])
reverse_string("racecar")
