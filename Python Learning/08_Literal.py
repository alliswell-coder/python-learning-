# ============================================================
# PYTHON LITERALS - Complete Guide
# ============================================================
# A literal is a fixed value written directly in source code.

# ------------------------------------------------------------
# 1. NUMERIC LITERALS
# ------------------------------------------------------------

# Integer literals
dec = 100           # decimal
oct_val = 0o17      # octal (prefix 0o)
hex_val = 0x1F      # hexadecimal (prefix 0x)
bin_val = 0b1010    # binary (prefix 0b)
big_num = 1_000_000 # underscores for readability

print("--- Integer Literals ---")
print(dec, oct_val, hex_val, bin_val, big_num)

# Float literals
f1 = 3.14
f2 = 2.5e3      # scientific: 2500.0
f3 = 1.2E-4     # 0.00012
f4 = .5         # same as 0.5

print("\n--- Float Literals ---")
print(f1, f2, f3, f4)

# Complex literals
c1 = 3 + 4j
c2 = 0 + 2j

print("\n--- Complex Literals ---")
print(c1, c2)

# ------------------------------------------------------------
# 2. STRING LITERALS
# ------------------------------------------------------------

s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single — can span
multiple lines'''
s4 = """triple double — also
multi-line"""

# Raw strings (backslashes treated literally — useful for regex/paths)
raw = r"C:\Users\karth\file.txt"    # \U and \f not treated as escapes

# Byte strings
b = b"hello bytes"

# f-strings (formatted string literals, Python 3.6+)
name = "SDET"
score = 99.5
fstr = f"Hello {name}, score = {score:.1f}"

# String with escape sequences
escaped = "tab:\there\nnewline"

print("\n--- String Literals ---")
print(s1)
print(s3)
print(raw)
print(b)
print(fstr)
print(escaped)

# String concatenation (implicit — adjacent string literals join automatically)
combined = "Hello" " " "World"
print(combined)

# ------------------------------------------------------------
# 3. BOOLEAN LITERALS
# ------------------------------------------------------------

t = True
f_val = False
print("\n--- Boolean Literals ---")
print(t, f_val, type(t))
print(True + True)   # 2  (bool is subclass of int)
print(False == 0)    # True

# ------------------------------------------------------------
# 4. NONE LITERAL
# ------------------------------------------------------------

nothing = None
print("\n--- None Literal ---")
print(nothing, type(nothing))
print(nothing is None)   # always use 'is' to check None

# ------------------------------------------------------------
# 5. LIST LITERALS  (mutable, ordered, allows duplicates)
# ------------------------------------------------------------

empty_list = []
nums = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]
nested = [[1, 2], [3, 4]]

print("\n--- List Literals ---")
print(nums)
print(mixed)
print(nested[1][0])   # 3

# ------------------------------------------------------------
# 6. TUPLE LITERALS  (immutable, ordered)
# ------------------------------------------------------------

empty_tuple = ()
single = (42,)          # trailing comma required for single-element tuple
coords = (10, 20)
rgb = (255, 128, 0)
packed = 1, 2, 3        # parentheses optional when packing

print("\n--- Tuple Literals ---")
print(single)
print(coords)
print(packed)

# ------------------------------------------------------------
# 7. DICTIONARY LITERALS  (mutable, key-value pairs)
# ------------------------------------------------------------

empty_dict = {}
person = {"name": "Karthik", "role": "SDET", "exp": 3}
mixed_keys = {1: "one", "two": 2, (3,): "tuple key"}

print("\n--- Dictionary Literals ---")
print(person)
print(person["role"])
print(mixed_keys[(3,)])

# ------------------------------------------------------------
# 8. SET LITERALS  (unordered, unique elements)
# ------------------------------------------------------------

# Note: {} creates a dict, NOT a set — use set() for empty set
empty_set = set()
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate removed

print("\n--- Set Literals ---")
print(fruits)           # 'apple' appears once
print(type(empty_set))

# ------------------------------------------------------------
# 9. ELLIPSIS LITERAL
# ------------------------------------------------------------

placeholder = ...       # same as Ellipsis object

def todo_function():
    ...                 # commonly used as a no-op placeholder

print("\n--- Ellipsis Literal ---")
print(placeholder, type(placeholder))

# Used in type hints for variable-length tuples
from typing import Tuple
def accept_any_length(t: Tuple[int, ...]) -> None:
    print(t)

accept_any_length((1, 2, 3, 4))

# ------------------------------------------------------------
# 10. SPECIAL NUMERIC LITERALS (Python 3.6+)
# ------------------------------------------------------------

inf = float('inf')          # positive infinity
neg_inf = float('-inf')     # negative infinity
nan = float('nan')          # Not a Number

print("\n--- Special Float Values ---")
print(inf, neg_inf, nan)
print(inf > 1_000_000)      # True
print(nan == nan)            # False — NaN is never equal to itself

# ------------------------------------------------------------
# SUMMARY TABLE
# ------------------------------------------------------------
print("\n--- Summary ---")
summary = {
    "Integer":  [100, 0b1010, 0o17, 0x1F],
    "Float":    [3.14, 2.5e3],
    "Complex":  [3+4j],
    "String":   ["hello", r"\raw", b"bytes", f"{name}"],
    "Boolean":  [True, False],
    "None":     [None],
    "List":     [[1, 2, 3]],
    "Tuple":    [(1, 2, 3)],
    "Dict":     [{"key": "value"}],
    "Set":      [{1, 2, 3}],
    "Ellipsis": [...],
}
for kind, examples in summary.items():
    print(f"  {kind:<10} -> {examples}")
