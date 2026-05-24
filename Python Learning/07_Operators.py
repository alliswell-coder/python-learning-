# ============================================================
# PYTHON OPERATORS - Complete Overview
# ============================================================
# An operator is a symbol that performs an operation on
# one or more operands (values or variables).
# ============================================================


# ------------------------------------------------------------
# 1. ARITHMETIC OPERATORS
# ------------------------------------------------------------
# Used to perform basic mathematical operations

a = 20
b = 6

print("--- Arithmetic Operators ---")
print(a + b)    # Addition       → 26
print(a - b)    # Subtraction    → 14
print(a * b)    # Multiplication → 120
print(a / b)    # Division       → 3.3333 (always float)
print(a // b)   # Floor Division → 3 (removes decimal)
print(a % b)    # Modulus        → 2 (remainder)
print(a ** b)   # Exponentiation → 64000000 (a to the power b)


# ------------------------------------------------------------
# 2. ASSIGNMENT OPERATORS
# ------------------------------------------------------------
# Used to assign values to variables

print("\n--- Assignment Operators ---")
x = 10          # Simple assignment
print(x)        # 10

x += 5          # x = x + 5  → 15
print(x)

x -= 3          # x = x - 3  → 12
print(x)

x *= 2          # x = x * 2  → 24
print(x)

x /= 4          # x = x / 4  → 6.0
print(x)

x //= 2         # x = x // 2 → 3.0
print(x)

x %= 2          # x = x % 2  → 1.0
print(x)

x = 3
x **= 3         # x = x ** 3 → 27
print(x)

x &= 5          # x = x & 5  → Bitwise AND
print(x)

x |= 4          # x = x | 4  → Bitwise OR
print(x)

x ^= 2          # x = x ^ 2  → Bitwise XOR
print(x)

x = 16
x >>= 2         # x = x >> 2 → Right shift
print(x)

x <<= 1         # x = x << 1 → Left shift
print(x)


# ------------------------------------------------------------
# 3. COMPARISON / RELATIONAL OPERATORS
# ------------------------------------------------------------
# Compare two values and return True or False

p = 10
q = 20

print("\n--- Comparison Operators ---")
print(p == q)   # Equal to            → False
print(p != q)   # Not equal to        → True
print(p > q)    # Greater than        → False
print(p < q)    # Less than           → True
print(p >= q)   # Greater or equal    → False
print(p <= q)   # Less or equal       → True
print(p >= 10)  # Greater or equal    → True (edge case)
print(p <= 10)  # Less or equal       → True (edge case)


# ------------------------------------------------------------
# 4. LOGICAL OPERATORS
# ------------------------------------------------------------
# Used to combine multiple conditions

m = True
n = False

print("\n--- Logical Operators ---")
print(m and n)      # Both must be True  → False
print(m or n)       # At least one True  → True
print(not m)        # Reverses the bool  → False
print(not n)        # Reverses the bool  → True

# Practical examples
age = 25
has_id = True
print(age >= 18 and has_id)     # True  — both conditions met
print(age < 18 or has_id)       # True  — one condition met
print(not has_id)                # False — reverses True


# ------------------------------------------------------------
# 5. BITWISE OPERATORS
# ------------------------------------------------------------
# Operate on binary (bit-level) representation of numbers

c = 12   # binary: 1100
d = 10   # binary: 1010

print("\n--- Bitwise Operators ---")
print(c & d)    # AND  → 1000 → 8   (both bits must be 1)
print(c | d)    # OR   → 1110 → 14  (at least one bit is 1)
print(c ^ d)    # XOR  → 0110 → 6   (bits must be different)
print(~c)       # NOT  → -(c+1) → -13 (flips all bits)
print(c << 2)   # Left Shift  → 110000 → 48 (multiply by 2^2)
print(c >> 2)   # Right Shift → 0011   → 3  (divide by 2^2)


# ------------------------------------------------------------
# 6. IDENTITY OPERATORS
# ------------------------------------------------------------
# Check if two variables point to the SAME object in memory
# (not just equal in value, but the exact same object)

print("\n--- Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1       # list3 points to the same object as list1

print(list1 is list3)       # True  — same object in memory
print(list1 is list2)       # False — same value but different objects
print(list1 is not list2)   # True  — different objects

# With small integers (Python caches -5 to 256)
num1 = 100
num2 = 100
print(num1 is num2)         # True  — cached integer object

num3 = 1000
num4 = 1000
print(num3 is num4)         # False — large integers not cached


# ------------------------------------------------------------
# 7. MEMBERSHIP OPERATORS
# ------------------------------------------------------------
# Check if a value exists inside a sequence (list, tuple, string, dict)

print("\n--- Membership Operators ---")
fruits = ["apple", "banana", "cherry"]
text = "Hello, Python!"
numbers = (1, 2, 3, 4, 5)
info = {"name": "Alice", "age": 25}

print("apple" in fruits)        # True  — apple is in the list
print("grape" in fruits)        # False — grape is not in the list
print("grape" not in fruits)    # True  — grape is not in the list
print("Python" in text)         # True  — substring check
print(3 in numbers)             # True  — value in tuple
print(10 not in numbers)        # True  — 10 is not in tuple
print("name" in info)           # True  — checks dictionary KEYS
print("Alice" in info)          # False — does not check values


# ------------------------------------------------------------
# 8. TERNARY / CONDITIONAL OPERATOR
# ------------------------------------------------------------
# One-line if-else expression
# Syntax: value_if_true  if  condition  else  value_if_false

print("\n--- Ternary Operator ---")
score = 75
result = "Pass" if score >= 50 else "Fail"
print(result)                           # Pass

temperature = 35
weather = "Hot" if temperature > 30 else "Cool"
print(weather)                          # Hot

num = -5
label = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(label)                            # Negative

# Ternary inside a function
def check_age(age):
    return "Adult" if age >= 18 else "Minor"

print(check_age(20))    # Adult
print(check_age(15))    # Minor


# ------------------------------------------------------------
# OPERATOR PRECEDENCE (High to Low)
# ------------------------------------------------------------
# Operators are evaluated in this order (like BODMAS in math):
#
# Priority | Operator          | Description
# ---------|-------------------|-----------------------------
#    1     | **                | Exponentiation
#    2     | ~  +  -           | Bitwise NOT, Unary plus/minus
#    3     | *  /  //  %       | Multiply, Divide, Floor, Modulus
#    4     | +  -              | Addition, Subtraction
#    5     | >>  <<            | Bitwise Shift
#    6     | &                 | Bitwise AND
#    7     | ^                 | Bitwise XOR
#    8     | |                 | Bitwise OR
#    9     | ==  !=  >  <  >= <=  is  is not  in  not in  | Comparisons
#   10     | not               | Logical NOT
#   11     | and               | Logical AND
#   12     | or                | Logical OR

print("\n--- Operator Precedence Example ---")
print(2 + 3 * 4)        # 14  — * before +
print((2 + 3) * 4)      # 20  — () overrides precedence
print(2 ** 3 + 1)       # 9   — ** before +
print(10 - 4 // 2)      # 8   — // before -
print(True or False and False)  # True — and before or
