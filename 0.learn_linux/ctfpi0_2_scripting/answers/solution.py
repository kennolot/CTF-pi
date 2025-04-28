import re # regular expression
# https://www.w3schools.com/python/python_regex.asp

with open("code.txt") as f:
    encoded = f.read()
print("Loaded encoded text:\n", encoded)
saved = re.findall("A(.)A", encoded)

print(saved)