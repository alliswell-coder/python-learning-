# ============================================================
# PYTHON STRINGS - Beginner Friendly Guide
# ============================================================
# A String is simply a sequence of characters inside quotes.
# Example: "Hello", 'Python', "123", "Karthik"
# ============================================================

# ------------------------------------------------------------
# 1. CREATING A STRING
# ------------------------------------------------------------
# You can use single quotes OR double quotes — both work!

name    = "Karthik"
course  = 'Python'
message = "I am learning Python!"

print(name)     # Karthik
print(course)   # Python
print(message)  # I am learning Python!

# ------------------------------------------------------------
# 2. PRINTING A STRING
# ------------------------------------------------------------
print("Hello, World!")
print("My name is", name)
print("I am learning", course)

# ------------------------------------------------------------
# 3. STRING LENGTH  — how many characters?
# ------------------------------------------------------------
# len() counts every character including spaces

word = "Python"
print(len(word))        # 6

sentence = "I love Python"
print(len(sentence))    # 13  (spaces are counted too!)

# ------------------------------------------------------------
# 4. ACCESSING CHARACTERS  — indexing
# ------------------------------------------------------------
# Think of a string like a list of boxes, each box has a number
# P  y  t  h  o  n
# 0  1  2  3  4  5    <- positive index (start from left)
#-6 -5 -4 -3 -2 -1    <- negative index (start from right)

lang = "Python"
print(lang[0])      # P  (first character)
print(lang[1])      # y
print(lang[-1])     # n  (last character)
print(lang[-2])     # o

# ------------------------------------------------------------
# 5. SLICING  — getting part of a string
# ------------------------------------------------------------
# Syntax:  string[start : end]
# NOTE: end index is NOT included

text = "Hello Python"
#       0123456789...

print(text[0:5])    # Hello  (index 0,1,2,3,4)
print(text[6:12])   # Python
print(text[:5])     # Hello  (start from beginning)
print(text[6:])     # Python (go till the end)
print(text[:])      # Hello Python (full string)
print(text[::2])    # Hlo yhn (every 2nd character)
print(text[::-1])   # nohtyP olleH (REVERSE the string!)

# ------------------------------------------------------------
# 6. STRING CONCATENATION  — joining strings
# ------------------------------------------------------------
# Use + to join two strings together

first = "Hello"
second = "World"
result = first + " " + second
print(result)       # Hello World

full_name = "Karthik" + " " + "Jadhav"
print(full_name)    # Karthik Jadhav

# ------------------------------------------------------------
# 7. STRING REPETITION  — repeat a string
# ------------------------------------------------------------
# Use * to repeat a string

print("Ha" * 3)         # HaHaHa
print("-" * 30)         # ------------------------------ (line separator)
print("Python! " * 2)   # Python! Python!

# ------------------------------------------------------------
# 8. UPPER AND LOWER CASE
# ------------------------------------------------------------
greeting = "hello world"

print(greeting.upper())         # HELLO WORLD
print(greeting.lower())         # hello world
print(greeting.capitalize())    # Hello world (only first letter)
print(greeting.title())         # Hello World (each word capitalized)
print("HELLO".swapcase())       # hello (swap upper <-> lower)

# ------------------------------------------------------------
# 9. STRIP  — removing extra spaces
# ------------------------------------------------------------
# Very useful when reading user input!

messy = "   Hello Python   "

print(messy.strip())    # "Hello Python"  (removes both sides)
print(messy.lstrip())   # "Hello Python   " (removes left side only)
print(messy.rstrip())   # "   Hello Python" (removes right side only)

# Remove specific characters
dotted = "***Hello***"
print(dotted.strip("*"))    # Hello

# ------------------------------------------------------------
# 10. REPLACE  — swap one word for another
# ------------------------------------------------------------
sentence = "I love Java"

print(sentence.replace("Java", "Python"))   # I love Python

# Replace only first occurrence
text2 = "cat and cat and cat"
print(text2.replace("cat", "dog", 1))       # dog and cat and cat

# ------------------------------------------------------------
# 11. SPLIT  — break string into a list
# ------------------------------------------------------------
# split() cuts the string wherever it finds the separator

fruits = "apple,banana,mango,grape"
print(fruits.split(","))    # ['apple', 'banana', 'mango', 'grape']

sentence2 = "Python is easy to learn"
print(sentence2.split())    # ['Python', 'is', 'easy', 'to', 'learn']

# limit how many splits
print(sentence2.split(" ", 2))  # ['Python', 'is', 'easy to learn']

# ------------------------------------------------------------
# 12. JOIN  — combine a list into a string (opposite of split)
# ------------------------------------------------------------
words = ["Python", "is", "awesome"]

print(" ".join(words))      # Python is awesome
print("-".join(words))      # Python-is-awesome
print(", ".join(words))     # Python, is, awesome

# ------------------------------------------------------------
# 13. FIND  — search for a word inside a string
# ------------------------------------------------------------
# find() returns the INDEX where it found the word
# returns -1 if NOT found

text3 = "I love Python programming"

print(text3.find("Python"))     # 7   (found at index 7)
print(text3.find("Java"))       # -1  (not found)
print(text3.count("o"))         # 2   (count how many times 'o' appears)

# ------------------------------------------------------------
# 14. STARTSWITH & ENDSWITH  — check beginning or end
# ------------------------------------------------------------
filename = "report_2024.pdf"

print(filename.startswith("report"))   # True
print(filename.endswith(".pdf"))       # True
print(filename.endswith(".jpg"))       # False

email = "karthicajadhav@outlook.com"
print(email.startswith("karthic"))     # True

# ------------------------------------------------------------
# 15. IN  — check if something exists in the string
# ------------------------------------------------------------
sentence3 = "Python is great for automation"

print("Python" in sentence3)        # True
print("Java" in sentence3)          # False
print("Java" not in sentence3)      # True

# ------------------------------------------------------------
# 16. F-STRINGS  — easy way to put variables inside strings
# ------------------------------------------------------------
# Put f before the string and use {} for variables

name2   = "Karthik"
role    = "SDET"
exp     = 3

print(f"My name is {name2}")
print(f"I am a {role} with {exp} years of experience")
print(f"2 + 2 = {2 + 2}")               # can do math inside {}
print(f"UPPER: {name2.upper()}")         # can call methods inside {}
print(f"Salary: {75000.50:.2f}")         # format to 2 decimal places

# ------------------------------------------------------------
# 17. STRING ALIGNMENT  — spacing and padding
# ------------------------------------------------------------
word2 = "Python"

print(word2.center(20))         #        Python
print(word2.center(20, "*"))    # *******Python*******
print(word2.ljust(20, "-"))     # Python--------------
print(word2.rjust(20, "-"))     # --------------Python
print("42".zfill(6))            # 000042 (pad with zeros)

# ------------------------------------------------------------
# 18. IS* METHODS  — check what kind of string it is
# ------------------------------------------------------------
print("Python3".isalnum())  # True  - only letters and numbers?
print("Python".isalpha())   # True  - only letters?
print("12345".isdigit())    # True  - only digits?
print("  ".isspace())       # True  - only spaces?
print("PYTHON".isupper())   # True  - all uppercase?
print("python".islower())   # True  - all lowercase?

# ------------------------------------------------------------
# 19. MULTILINE STRINGS  — strings across many lines
# ------------------------------------------------------------
address = """
Name   : Karthik Jadhav
Role   : SDET
City   : Pune
Course : Python
"""
print(address)

# Useful for SQL queries or long messages
query = """
SELECT name, role
FROM employees
WHERE department = 'QA'
"""
print(query)

# ------------------------------------------------------------
# 20. ESCAPE CHARACTERS  — special characters in strings
# ------------------------------------------------------------
print("Hello\tWorld")       # \t = TAB
print("Hello\nWorld")       # \n = NEW LINE
print("She said \"Hello\"") # \" = double quote inside string
print("C:\\Users\\karth")   # \\ = backslash

# Raw string — ignores escape characters (great for file paths!)
path = r"C:\Users\karth\Desktop"
print(path)                 # C:\Users\karth\Desktop

# ------------------------------------------------------------
# 21. CONVERTING TO STRING
# ------------------------------------------------------------
age    = 25
height = 5.9
flag   = True

print(str(age))     # "25"
print(str(height))  # "5.9"
print(str(flag))    # "True"

# Why needed? You can't join string + number directly:
# print("Age: " + age)  <- ERROR!
print("Age: " + str(age))   # Works!

# ------------------------------------------------------------
# QUICK REFERENCE — All String Methods
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("  STRING METHODS - QUICK REFERENCE")
print("=" * 50)
reference = {
    "upper()":          "HELLO -> HELLO",
    "lower()":          "HELLO -> hello",
    "title()":          "hello world -> Hello World",
    "capitalize()":     "hello -> Hello",
    "strip()":          "remove spaces from both sides",
    "lstrip()":         "remove spaces from left",
    "rstrip()":         "remove spaces from right",
    "replace(a,b)":     "swap 'a' with 'b'",
    "split(x)":         "break string into list",
    "join(list)":       "combine list into string",
    "find(x)":          "find index of x (-1 if not found)",
    "count(x)":         "count how many times x appears",
    "startswith(x)":    "does string start with x?",
    "endswith(x)":      "does string end with x?",
    "len()":            "total number of characters",
    "in":               "check if value exists in string",
    "isalpha()":        "only letters? True/False",
    "isdigit()":        "only digits? True/False",
    "isalnum()":        "only letters & digits? True/False",
    "center(n)":        "center the text in n spaces",
    "ljust(n)":         "align left in n spaces",
    "rjust(n)":         "align right in n spaces",
    "zfill(n)":         "pad with zeros on the left",
}
for method, desc in reference.items():
    print(f"  {method:<20} -> {desc}")

# ------------------------------------------------------------
# 22. STRING COMPARISON  — comparing two strings
# ------------------------------------------------------------
# Python compares strings alphabetically (like a dictionary)

print("\n--- String Comparison ---")
print("apple" == "apple")   # True
print("apple" == "Apple")   # False  (case sensitive!)
print("apple" != "mango")   # True
print("apple" < "mango")    # True   (a comes before m)
print("zebra" > "ant")      # True   (z comes after a)

# Tip: always convert to same case before comparing
input1 = "Python"
input2 = "python"
print(input1.lower() == input2.lower())     # True  (safe comparison)

# ------------------------------------------------------------
# 23. STRINGS ARE IMMUTABLE  — you cannot change a character
# ------------------------------------------------------------
# Once created, a string cannot be modified directly
# You must create a NEW string

print("\n--- String Immutability ---")
word = "Python"
# word[0] = "J"   <- This will give an ERROR!

# Instead, build a new string
new_word = "J" + word[1:]
print(new_word)     # Jython

# replace() also creates a new string
original = "I love Java"
updated  = original.replace("Java", "Python")
print(original)     # I love Java  (unchanged)
print(updated)      # I love Python

# ------------------------------------------------------------
# 24. LOOPING THROUGH A STRING
# ------------------------------------------------------------
# You can go through each character one by one using a for loop

print("\n--- Loop Through String ---")
for char in "Python":
    print(char, end=" ")    # P y t h o n
print()

# Loop with index number
for i, char in enumerate("SDET"):
    print(f"Index {i} -> {char}")

# Count vowels using a loop
vowels = 0
for char in "automation testing":
    if char in "aeiou":
        vowels += 1
print(f"Vowels found: {vowels}")

# ------------------------------------------------------------
# 25. STRING + LIST  — converting between the two
# ------------------------------------------------------------
print("\n--- String <-> List ---")

# String to list of characters
chars = list("Python")
print(chars)            # ['P', 'y', 't', 'h', 'o', 'n']

# List back to string
print("".join(chars))   # Python

# Split sentence into word list
words2 = "learn python for sdet".split()
print(words2)           # ['learn', 'python', 'for', 'sdet']

# Join back
print(" ".join(words2)) # learn python for sdet

# ------------------------------------------------------------
# 26. PARTITION  — split into exactly 3 parts
# ------------------------------------------------------------
# Returns (before, separator, after)  — always 3 parts

print("\n--- partition() ---")
email = "karthicajadhav@outlook.com"
parts = email.partition("@")
print(parts)            # ('karthicajadhav', '@', 'outlook.com')
print(parts[0])         # karthicajadhav  (username)
print(parts[2])         # outlook.com     (domain)

text4 = "first:second:third"
print(text4.partition(":"))     # ('first', ':', 'second:third')
print(text4.rpartition(":"))    # ('first:second', ':', 'third')

# ------------------------------------------------------------
# 27. ord() AND chr()  — characters and numbers
# ------------------------------------------------------------
# Every character has a number (ASCII / Unicode code)
# ord() -> character to number
# chr() -> number to character

print("\n--- ord() and chr() ---")
print(ord("A"))     # 65
print(ord("a"))     # 97
print(ord("0"))     # 48
print(chr(65))      # A
print(chr(97))      # a
print(chr(80))      # P

# Print A to Z using chr and a loop
print("Alphabet: ", end="")
for i in range(65, 91):
    print(chr(i), end=" ")
print()

# ------------------------------------------------------------
# 28. PALINDROME CHECK  — reads same forwards and backwards
# ------------------------------------------------------------
print("\n--- Palindrome Check ---")

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # ignore case and spaces
    return s == s[::-1]

print(is_palindrome("racecar"))     # True
print(is_palindrome("madam"))       # True
print(is_palindrome("Python"))      # False
print(is_palindrome("Never odd or even"))  # True

# ------------------------------------------------------------
# 29. COUNT WORDS AND CHARACTERS
# ------------------------------------------------------------
print("\n--- Count Words & Characters ---")
text5 = "Python is great for automation testing"

word_count = len(text5.split())
char_count = len(text5)
char_no_space = len(text5.replace(" ", ""))

print(f"Words     : {word_count}")
print(f"Characters: {char_count}")
print(f"No spaces : {char_no_space}")

# ------------------------------------------------------------
# 30. REAL WORLD EXAMPLES (SDET Use Cases)
# ------------------------------------------------------------
print("\n--- Real World / SDET Examples ---")

# Check if email is valid (basic check)
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

print(is_valid_email("karthic@outlook.com"))    # True
print(is_valid_email("karthicoutlook.com"))     # False
print(is_valid_email("karthic@outlookcom"))     # False

# Extract file extension
filename = "test_report_2024.pdf"
ext = filename.split(".")[-1]
print(f"Extension: {ext}")      # pdf

# Check if a URL contains a keyword
url = "https://www.example.com/login?user=admin"
print("login" in url)           # True
print(url.startswith("https"))  # True  (secure URL check)

# Parse a CSV-like test data line
test_data = "TC001,Login Test,Pass,3.2s"
tc_id, tc_name, status, duration = test_data.split(",")
print(f"Test: {tc_name} | Status: {status} | Time: {duration}")

# Clean up test output (remove extra whitespace)
raw_output = "  ERROR: element not found   "
clean = raw_output.strip()
print(repr(clean))      # 'ERROR: element not found'
