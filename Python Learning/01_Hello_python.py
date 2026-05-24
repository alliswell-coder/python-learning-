# ============================================================
# HELLO WORLD IN PYTHON - Complete Guide
# ============================================================

# ------------------------------------------------------------
# 1. BASIC HELLO WORLD
# ------------------------------------------------------------
print("Hello, World!")
print('Hello, World!')          # single quotes work too

# ------------------------------------------------------------
# 2. PRINT WITH VARIABLES
# ------------------------------------------------------------
message = "Hello, World!"
print(message)

name = "Karthik"
print("Hello,", name)           # Hello, Karthik

# ------------------------------------------------------------
# 3. PRINT MULTIPLE VALUES
# ------------------------------------------------------------
print("Hello", "World", "from", "Python")   # separated by space by default

# ------------------------------------------------------------
# 4. PRINT WITH sep (custom separator)
# ------------------------------------------------------------
print("Hello", "World", sep="-")    # Hello-World
print("Hello", "World", sep="")     # HelloWorld
print("Hello", "World", sep=", ")   # Hello, World

# ------------------------------------------------------------
# 5. PRINT WITH end (custom line ending)
# ------------------------------------------------------------
print("Hello", end=" ")
print("World")                      # prints on same line: Hello World

print("Line 1", end="\n\n")         # adds extra blank line
print("Line 2")

# ------------------------------------------------------------
# 6. PRINT MULTIPLE LINES
# ------------------------------------------------------------
print("Hello\nWorld\nFrom Python")  # \n = new line

print("""
Hello
World
From Python
""")                                # triple quotes for multiline

# ------------------------------------------------------------
# 7. PRINT WITH F-STRING
# ------------------------------------------------------------
name = "Karthik"
role = "SDET"
print(f"Hello, {name}! You are a {role}.")

# ------------------------------------------------------------
# 8. PRINT WITH .format()
# ------------------------------------------------------------
print("Hello, {}! You are a {}.".format(name, role))

# ------------------------------------------------------------
# 9. PRINT NUMBERS AND EXPRESSIONS
# ------------------------------------------------------------
print(10 + 20)              # 30
print(f"10 + 20 = {10+20}") # 10 + 20 = 30

# ------------------------------------------------------------
# 10. PRINT WITH SPECIAL CHARACTERS
# ------------------------------------------------------------
print("Hello\tWorld")       # tab space
print("Hello \"World\"")    # quotes inside string
print("Hello \\World")      # backslash

# ------------------------------------------------------------
# 11. PRINT TO CHECK TYPE
# ------------------------------------------------------------
print(type("Hello, World!"))    # <class 'str'>
print(type(42))                 # <class 'int'>
print(type(3.14))               # <class 'float'>

# ------------------------------------------------------------
# 12. COMMENT STYLES IN PYTHON
# ------------------------------------------------------------
# This is a single-line comment

"""
This is a
multi-line comment
(technically a docstring)
"""

# ------------------------------------------------------------
# 13. HELLO WORLD INSIDE A FUNCTION
# ------------------------------------------------------------
def say_hello():
    print("Hello, World!")

def greet(name):
    print(f"Hello, {name}!")

say_hello()
greet("Karthik")

# ------------------------------------------------------------
# 14. HELLO WORLD — input from user
# ------------------------------------------------------------
# Uncomment below to try interactive input
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# ------------------------------------------------------------
# 15. PYTHON VERSION CHECK
# ------------------------------------------------------------
import sys
print(f"\nPython version: {sys.version}")
print(f"Hello from Python {sys.version_info.major}.{sys.version_info.minor}!")
