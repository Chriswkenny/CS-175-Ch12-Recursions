#Christopher Kenny
#CS 175
#Q: Write a python program using recursion to check if a string is a palindrome

def palindrome_checker(word):
  if len(word) <= 1:
    return True
  elif word[0] == word[-1]:
    return palindrome_checker(word[1:-1])
  else:
    return False

palindrome_checker("racecar")
