import re

def wordstart(string, pattern):
    if re.match(f"^{pattern}", string):
        return True
    else:
        return False


string =input("Enter a string:")
word = input("Enter a word to check")
print(wordstart(string, word))
