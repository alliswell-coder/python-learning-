# ============================================================
# Python Dictionaries - Complete Guide
# ============================================================

# ── 1. Creating Dictionaries ─────────────────────────────────
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
using_constructor = dict(name="Bob", age=25, city="London")
from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])

print("=== Creating Dictionaries ===")
print(person)
print(using_constructor)
print(from_pairs)

# ── 2. Accessing Values ──────────────────────────────────────
print("\n=== Accessing Values ===")
print(person["name"])           # Direct access → 'Alice'
print(person.get("age"))        # Safe access → 30
print(person.get("email", "N/A"))  # Default if key missing → 'N/A'

# ── 3. Adding & Updating ─────────────────────────────────────
print("\n=== Adding & Updating ===")
person["email"] = "alice@example.com"   # Add new key
person["age"] = 31                      # Update existing key
person.update({"city": "Boston", "phone": "555-1234"})  # Bulk update
print(person)

# ── 4. Removing Items ────────────────────────────────────────
print("\n=== Removing Items ===")
removed = person.pop("phone")           # Remove & return value
print(f"Removed: {removed}")
person.popitem()                        # Remove last inserted item
del person["email"]                     # Delete by key
print(person)

temp = {"x": 10, "y": 20}
temp.clear()                            # Remove all items
print(f"After clear: {temp}")

# ── 5. Dictionary Methods ────────────────────────────────────
data = {"name": "Alice", "age": 31, "city": "Boston"}

print("\n=== Dictionary Methods ===")
print("Keys:  ", list(data.keys()))     # All keys
print("Values:", list(data.values()))   # All values
print("Items: ", list(data.items()))    # Key-value pairs as tuples

# ── 6. Iterating ─────────────────────────────────────────────
print("\n=== Iterating ===")
for key in data:
    print(f"  {key}: {data[key]}")

for key, value in data.items():
    print(f"  {key} → {value}")

# ── 7. Membership Check ──────────────────────────────────────
print("\n=== Membership Check ===")
print("name" in data)       # True
print("salary" in data)     # False
print("salary" not in data) # True

# ── 8. Dictionary Comprehension ──────────────────────────────
print("\n=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)

evens = {k: v for k, v in squares.items() if v % 2 == 0}
print("Even squares:", evens)

words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

# ── 9. Nested Dictionaries ───────────────────────────────────
print("\n=== Nested Dictionaries ===")
employees = {
    "emp1": {"name": "Alice", "dept": "QA",      "salary": 70000},
    "emp2": {"name": "Bob",   "dept": "Dev",     "salary": 80000},
    "emp3": {"name": "Carol", "dept": "DevOps",  "salary": 75000},
}
print(employees["emp1"]["name"])        # Alice
employees["emp2"]["salary"] = 85000    # Update nested value

for emp_id, info in employees.items():
    print(f"  {emp_id}: {info['name']} | {info['dept']} | ${info['salary']}")

# ── 10. setdefault ───────────────────────────────────────────
print("\n=== setdefault ===")
config = {"host": "localhost"}
config.setdefault("port", 8080)         # Key absent → sets default
config.setdefault("host", "remote")    # Key present → no change
print(config)

# ── 11. Merging Dictionaries ─────────────────────────────────
print("\n=== Merging Dictionaries ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}

merged_update = {**dict1, **dict2}         # Unpack merge (dict2 wins on conflict)
print("Unpacked merge:", merged_update)

merged_or = dict1 | dict2                  # | operator (Python 3.9+)
print("| merge:       ", merged_or)

dict1 |= {"d": 4}                          # In-place merge (Python 3.9+)
print("|= in-place:   ", dict1)

# ── 12. Copying ──────────────────────────────────────────────
print("\n=== Copying ===")
import copy

original = {"x": [1, 2, 3], "y": 10}
shallow = original.copy()              # Shallow copy
deep    = copy.deepcopy(original)      # Deep copy

shallow["x"].append(99)   # Mutates original's list too
deep["x"].append(100)     # Does NOT affect original

print("Original after shallow mutation:", original)
print("Deep copy (independent):        ", deep)

# ── 13. Useful Built-ins with Dicts ─────────────────────────
print("\n=== Useful Built-ins ===")
scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95}

print("Length:  ", len(scores))
print("Max key: ", max(scores))                          # Alphabetically last key
print("Max val: ", max(scores, key=lambda k: scores[k]))# Key with highest value
print("Min val: ", min(scores, key=lambda k: scores[k]))
print("Sorted:  ", sorted(scores.items(), key=lambda x: x[1], reverse=True))

# ── 14. fromkeys ─────────────────────────────────────────────
print("\n=== fromkeys ===")
keys = ["a", "b", "c", "d"]
initialized = dict.fromkeys(keys, 0)   # All keys start at 0
print(initialized)

# ── 15. Practical SDET Example – Test Case Registry ─────────
print("\n=== Practical SDET Example: Test Case Registry ===")
test_cases = {
    "TC001": {"name": "Login valid user",      "status": "PASS", "duration_s": 1.2},
    "TC002": {"name": "Login invalid password","status": "FAIL", "duration_s": 0.8},
    "TC003": {"name": "Add item to cart",      "status": "PASS", "duration_s": 2.5},
    "TC004": {"name": "Checkout flow",         "status": "SKIP", "duration_s": 0.0},
}

passed = [tc for tc, info in test_cases.items() if info["status"] == "PASS"]
failed = [tc for tc, info in test_cases.items() if info["status"] == "FAIL"]
total_time = sum(info["duration_s"] for info in test_cases.values())

print(f"  Total tests : {len(test_cases)}")
print(f"  Passed      : {passed}")
print(f"  Failed      : {failed}")
print(f"  Total time  : {total_time:.1f}s")
