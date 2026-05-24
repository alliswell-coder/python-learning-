# ============================================================
# PYTHON LIST & TUPLE - Beginner Friendly Guide
# ============================================================
# LIST  -> mutable   (you CAN change it)    -> uses [ ]
# TUPLE -> immutable (you CANNOT change it) -> uses ( )
# ============================================================

# ============================================================
#                        L I S T S
# ============================================================

# ------------------------------------------------------------
# 1. CREATING A LIST
# ------------------------------------------------------------
fruits      = ["apple", "banana", "mango", "grape"]
numbers     = [10, 20, 30, 40, 50]
mixed       = ["Karthik", 25, True, 3.14]
empty_list  = []
test_case   = ["TC001", "login", "logout", "pass", "3.2s"]

print("--- Creating Lists ---")
print(fruits)
print(numbers)
print(test_case)

# ------------------------------------------------------------
# 2. ACCESSING ITEMS — indexing
# ------------------------------------------------------------
# Index starts at 0 (first item)
# Negative index starts from the end (-1 = last item)

print("\n--- Accessing Items ---")
print(test_case[0])     # TC001  (first)
print(test_case[1])     # login
print(test_case[2])     # logout
print(test_case[3])     # pass
print(test_case[4])     # 3.2s
print(test_case[-1])    # 3.2s  (last item)
print(test_case[-2])    # pass  (second from last)

# ------------------------------------------------------------
# 3. SLICING A LIST — get part of a list
# ------------------------------------------------------------
# Syntax: list[start : end]   NOTE: end is NOT included

print("\n--- Slicing ---")
print(test_case[1:3])   # ['login', 'logout']  start=1, end before 3
print(test_case[:2])    # ['TC001', 'login']   from beginning
print(test_case[2:])    # ['logout', 'pass', '3.2s'] till end
print(test_case[::-1])  # reversed list

nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[0:3])        # [10, 20, 30]
print(nums[::2])        # [10, 30, 50, 70] every 2nd item

# ------------------------------------------------------------
# 4. LIST LENGTH
# ------------------------------------------------------------
print("\n--- Length ---")
print(len(fruits))          # 4
print(len(test_case))       # 5
print(len(empty_list))      # 0

# ------------------------------------------------------------
# 5. ADDING ITEMS TO A LIST
# ------------------------------------------------------------
print("\n--- Adding Items ---")
colors = ["red", "green"]
print("Before:", colors)

colors.append("blue")               # add to the END
print("After append:", colors)

colors.insert(1, "yellow")          # insert at index 1
print("After insert:", colors)

colors.extend(["pink", "white"])    # add multiple items
print("After extend:", colors)

# ------------------------------------------------------------
# 6. REMOVING ITEMS FROM A LIST
# ------------------------------------------------------------
print("\n--- Removing Items ---")
animals = ["cat", "dog", "bird", "fish", "dog"]
print("Before:", animals)

animals.remove("bird")      # remove by VALUE (first match)
print("After remove:", animals)

popped = animals.pop()      # remove LAST item and return it
print("Popped:", popped)
print("After pop:", animals)

animals.pop(0)              # remove item at specific index
print("After pop(0):", animals)

del animals[0]              # delete item at index
print("After del:", animals)

# ------------------------------------------------------------
# 7. UPDATING / CHANGING ITEMS
# ------------------------------------------------------------
print("\n--- Updating Items ---")
skills = ["manual", "selenium", "java"]
print("Before:", skills)

skills[2] = "python"        # replace index 2
print("After update:", skills)

# ------------------------------------------------------------
# 8. CHECKING IF ITEM EXISTS
# ------------------------------------------------------------
print("\n--- Check Item Exists ---")
tools = ["selenium", "pytest", "postman", "jira"]

print("selenium" in tools)      # True
print("jenkins" in tools)       # False
print("jenkins" not in tools)   # True

# ------------------------------------------------------------
# 9. SORTING & REVERSING
# ------------------------------------------------------------
print("\n--- Sorting & Reversing ---")
scores = [45, 12, 89, 33, 67]

scores.sort()                   # sort ascending
print("Sorted asc:", scores)

scores.sort(reverse=True)       # sort descending
print("Sorted desc:", scores)

names = ["Zara", "Alice", "Mike", "Bob"]
names.sort()                    # alphabetical
print("Names sorted:", names)

numbers2 = [1, 2, 3, 4, 5]
numbers2.reverse()              # reverse the order
print("Reversed:", numbers2)

# sorted() — does NOT change original, returns new list
original = [5, 3, 8, 1]
new_sorted = sorted(original)
print("Original:", original)    # unchanged
print("New sorted:", new_sorted)

# ------------------------------------------------------------
# 10. OTHER USEFUL LIST METHODS
# ------------------------------------------------------------
print("\n--- Other Methods ---")
nums2 = [10, 20, 30, 20, 40, 20]

print(nums2.count(20))      # 3  — how many times 20 appears
print(nums2.index(30))      # 2  — index of first 30

copy_list = nums2.copy()    # make a copy
print("Copy:", copy_list)

nums2.clear()               # remove ALL items
print("After clear:", nums2)

# ------------------------------------------------------------
# 11. LOOPING THROUGH A LIST
# ------------------------------------------------------------
print("\n--- Looping ---")
fruits2 = ["apple", "banana", "mango"]

# Simple loop
for fruit in fruits2:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits2):
    print(f"{i} -> {fruit}")

# ------------------------------------------------------------
# 12. LIST COMPREHENSION — shorter way to create lists
# ------------------------------------------------------------
print("\n--- List Comprehension ---")

# Normal way
squares = []
for n in range(1, 6):
    squares.append(n * n)
print("Normal:", squares)

# Shorter way — one line!
squares2 = [n * n for n in range(1, 6)]
print("Comprehension:", squares2)

# With condition — only even numbers
evens = [n for n in range(1, 11) if n % 2 == 0]
print("Evens:", evens)

# Uppercase all items in a list
words = ["selenium", "pytest", "postman"]
upper = [w.upper() for w in words]
print("Upper:", upper)

# ------------------------------------------------------------
# 13. NESTED LIST — list inside a list
# ------------------------------------------------------------
print("\n--- Nested List ---")
test_data = [
    ["TC001", "Login",   "Pass"],
    ["TC002", "Logout",  "Pass"],
    ["TC003", "Signup",  "Fail"],
]

print(test_data[0])         # ['TC001', 'Login', 'Pass']
print(test_data[1][1])      # Logout

for tc in test_data:
    print(f"ID: {tc[0]} | Name: {tc[1]} | Status: {tc[2]}")

# ============================================================
#                       T U P L E S
# ============================================================

# ------------------------------------------------------------
# 14. CREATING A TUPLE
# ------------------------------------------------------------
# Tuples are like lists BUT cannot be changed after creation
# Use ( ) instead of [ ]

print("\n--- Creating Tuples ---")
coords      = (10, 20)
rgb         = (255, 128, 0)
person      = ("Karthik", "SDET", 3)
single      = (42,)         # single item needs trailing comma!
empty_tuple = ()

print(coords)
print(rgb)
print(person)
print(single)

# Without parentheses also works
packed = 1, 2, 3
print(packed)           # (1, 2, 3)
print(type(packed))     # <class 'tuple'>

# ------------------------------------------------------------
# 15. ACCESSING TUPLE ITEMS
# ------------------------------------------------------------
print("\n--- Accessing Tuple Items ---")
colors_t = ("red", "green", "blue", "yellow")

print(colors_t[0])      # red   (first)
print(colors_t[-1])     # yellow (last)
print(colors_t[1:3])    # ('green', 'blue')

# ------------------------------------------------------------
# 16. TUPLE IS IMMUTABLE — cannot change items
# ------------------------------------------------------------
print("\n--- Tuple Immutability ---")
point = (5, 10)
# point[0] = 99   <- This gives ERROR!

# To "update" a tuple — convert to list, change, convert back
point_list = list(point)
point_list[0] = 99
point = tuple(point_list)
print(point)            # (99, 10)

# ------------------------------------------------------------
# 17. TUPLE METHODS
# ------------------------------------------------------------
print("\n--- Tuple Methods ---")
nums_t = (10, 20, 30, 20, 40, 20)

print(nums_t.count(20))     # 3  — how many times 20 appears
print(nums_t.index(30))     # 2  — index of first 30
print(len(nums_t))          # 6  — total items

# ------------------------------------------------------------
# 18. TUPLE UNPACKING — assign values to variables
# ------------------------------------------------------------
print("\n--- Tuple Unpacking ---")
name2, role, exp = ("Karthik", "SDET", 3)
print(name2)    # Karthik
print(role)     # SDET
print(exp)      # 3

# Swap two variables — Python trick!
a, b = 10, 20
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After:  a={a}, b={b}")

# Capture remaining items with *
first, *rest = (1, 2, 3, 4, 5)
print(f"First: {first}, Rest: {rest}")

# ------------------------------------------------------------
# 19. LOOPING THROUGH A TUPLE
# ------------------------------------------------------------
print("\n--- Looping Through Tuple ---")
tools_t = ("selenium", "pytest", "postman", "jira")

for i, tool in enumerate(tools_t, start=1):
    print(f"{i}. {tool}")

# ------------------------------------------------------------
# 20. CONVERT BETWEEN LIST AND TUPLE
# ------------------------------------------------------------
print("\n--- Convert List <-> Tuple ---")
my_list  = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)           # list -> tuple
print(my_tuple, type(my_tuple))

back_list = list(my_tuple)          # tuple -> list
print(back_list, type(back_list))

# ------------------------------------------------------------
# 21. LIST vs TUPLE — quick comparison
# ------------------------------------------------------------
print("\n--- List vs Tuple ---")
print(f"{'Feature':<15} | {'List [ ]':<22} | {'Tuple ( )'}")
print("-" * 55)
print(f"{'Changeable?':<15} | {'YES (mutable)':<22} | NO (immutable)")
print(f"{'Syntax':<15} | {'[ ]':<22} | ( )")
print(f"{'Speed':<15} | {'Slower':<22} | Faster")
print(f"{'Use when':<15} | {'Data may change':<22} | Data stays fixed")
print(f"{'Example':<15} | {'test results':<22} | x,y coordinates")

# ------------------------------------------------------------
# 22. REAL WORLD / SDET EXAMPLES
# ------------------------------------------------------------
print("\n--- SDET Real World Examples ---")

# Build and manage a test suite
test_suite = ["login_test", "logout_test", "signup_test"]
test_suite.append("password_reset_test")
print("Test Suite:", test_suite)
print("Total Tests:", len(test_suite))

# Find failed tests
all_tests = ["TC001", "TC002", "TC003", "TC004", "TC005"]
passed    = ["TC001", "TC002", "TC004"]
failed    = [tc for tc in all_tests if tc not in passed]
print("Failed Tests:", failed)

# Config as tuple (should never change!)
DB_CONFIG = ("localhost", 5432, "testdb")
host, port, db = DB_CONFIG
print(f"DB -> Host: {host} | Port: {port} | DB: {db}")

# Cross-browser testing loop
browsers = ["chrome", "firefox", "edge"]
for browser in browsers:
    print(f"Running tests on: {browser.upper()}")

# Sort test results by duration
results = [("TC003", 2.1), ("TC001", 5.4), ("TC002", 1.2)]
results.sort(key=lambda x: x[1])
print("\nTests sorted by duration (fastest first):")
for tc, duration in results:
    print(f"  {tc} -> {duration}s")
