# ============================================================
# PYTHON IDENTIFIERS - Complete Overview
# ============================================================
# An identifier is a name given to variables, functions,
# classes, modules, or any other object in Python.
#
# Rules for Identifiers:
# 1. Can contain letters (a-z, A-Z), digits (0-9), underscore (_)
# 2. Cannot start with a digit
# 3. Cannot use reserved keywords
# 4. Case-sensitive (name != Name != NAME)
# 5. No special characters allowed (!@#$%^&*)
# ============================================================


# ------------------------------------------------------------
# 1. VARIABLE IDENTIFIERS
# ------------------------------------------------------------
name = "Alice"                  # string variable
age = 25                        # integer variable
height = 5.6                    # float variable
is_active = True                # boolean variable
data = None                     # NoneType variable
scores = [90, 85, 78]           # list variable
coordinates = (10.5, 20.3)      # tuple variable
student_info = {"name": "Bob"}  # dictionary variable
unique_ids = {101, 102, 103}    # set variable


# ------------------------------------------------------------
# 2. CONSTANT IDENTIFIERS (by convention: ALL_CAPS)
# ------------------------------------------------------------
PI = 3.14159
MAX_SIZE = 100
MIN_VALUE = 0
BASE_URL = "https://example.com"
APP_NAME = "MyApp"
TAX_RATE = 0.18
GRAVITY = 9.8


# ------------------------------------------------------------
# 3. FUNCTION IDENTIFIERS
# ------------------------------------------------------------
def greet():
    print("Hello, World!")

def add_numbers(a, b):
    return a + b

def calculate_area(length, width):
    return length * width

def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def is_even(number):
    return number % 2 == 0

def find_maximum(num_list):
    return max(num_list)


# ------------------------------------------------------------
# 4. CLASS IDENTIFIERS (PascalCase by convention)
# ------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name        # instance variable identifier
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}")


class BankAccount:
    bank_name = "Global Bank"   # class variable identifier

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class ElectricCar(BankAccount):  # Inherited class identifier
    def __init__(self, owner, balance, battery):
        super().__init__(owner, balance)
        self.battery = battery


# ------------------------------------------------------------
# 5. PRIVATE IDENTIFIERS (Single underscore prefix _)
#    Convention: meant for internal use only
# ------------------------------------------------------------
class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"   # protected
        self.__private_var = "I am private"      # name-mangled

    def _helper_method(self):                    # protected method
        return "Helper logic here"

    def __secret_method(self):                   # private method
        return "Secret logic here"

    def show(self):
        print(self._helper_method())
        print(self.__secret_method())            # accessed via public method


# ------------------------------------------------------------
# 6. DUNDER / MAGIC IDENTIFIERS (Double underscore on both sides)
# ------------------------------------------------------------
class Vector:
    def __init__(self, x, y):       # __init__ : constructor
        self.x = x
        self.y = y

    def __str__(self):              # __str__  : string representation
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):             # __repr__ : official representation
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):       # __add__  : + operator overload
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):              # __len__  : len() support
        return 2

    def __eq__(self, other):        # __eq__   : == operator overload
        return self.x == other.x and self.y == other.y


# ------------------------------------------------------------
# 7. LOOP VARIABLE IDENTIFIERS
# ------------------------------------------------------------
for index in range(5):
    pass

for item in scores:
    pass

for key, value in student_info.items():
    pass

count = 0
while count < 5:
    count += 1


# ------------------------------------------------------------
# 8. LAMBDA IDENTIFIERS (Anonymous function assigned to variable)
# ------------------------------------------------------------
square = lambda x: x ** 2
cube = lambda x: x ** 3
add = lambda a, b: a + b
is_positive = lambda n: n > 0


# ------------------------------------------------------------
# 9. IMPORT / ALIAS IDENTIFIERS
# ------------------------------------------------------------
import math                    # module identifier
import os as operating_system  # alias identifier
import sys

from math import pi as PI_VALUE  # imported name with alias


# ------------------------------------------------------------
# 10. EXCEPTION IDENTIFIERS
# ------------------------------------------------------------
try:
    result = 10 / 0
except ZeroDivisionError as error:      # exception identifier
    print(f"Error caught: {error}")
except (TypeError, ValueError) as err:  # multiple exception identifier
    print(f"Type/Value error: {err}")
finally:
    pass


# ------------------------------------------------------------
# 11. COMPREHENSION IDENTIFIERS
# ------------------------------------------------------------
squared_list = [x ** 2 for x in range(10)]           # list comprehension
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
square_dict = {x: x ** 2 for x in range(5)}          # dict comprehension
square_set = {x ** 2 for x in range(5)}              # set comprehension
square_gen = (x ** 2 for x in range(5))              # generator expression


# ------------------------------------------------------------
# 12. GLOBAL & LOCAL IDENTIFIERS
# ------------------------------------------------------------
global_counter = 0              # global identifier

def update_counter():
    global global_counter       # referencing global identifier
    local_temp = 10             # local identifier (only inside function)
    global_counter += local_temp


# ------------------------------------------------------------
# 13. PARAMETER IDENTIFIERS (in function definitions)
# ------------------------------------------------------------
def regular_params(param1, param2):         # positional parameters
    pass

def default_params(x, y=10, z=20):         # default value parameters
    pass

def args_params(*args):                     # variable positional params
    pass

def kwargs_params(**kwargs):                # variable keyword params
    pass

def mixed_params(a, b, *args, **kwargs):   # mixed parameters
    pass


# ------------------------------------------------------------
# 14. VALID vs INVALID IDENTIFIER EXAMPLES
# ------------------------------------------------------------
# VALID identifiers:
my_var = 1
_var = 2
__var = 3
var123 = 4
MyClass2 = None
camelCaseVar = 5
snake_case_var = 6

# INVALID identifiers (commented out — would cause SyntaxError):
# 2var = 1        # Cannot start with digit
# my-var = 2      # Hyphens not allowed
# my var = 3      # Spaces not allowed
# class = 4       # Reserved keyword
# @var = 5        # Special characters not allowed


# ------------------------------------------------------------
# 15. CASE SENSITIVITY OF IDENTIFIERS
# ------------------------------------------------------------
value = 10        # three DIFFERENT identifiers
Value = 20
VALUE = 30

print(value, Value, VALUE)   # Output: 10 20 30


# ------------------------------------------------------------
# SUMMARY TABLE (as comments)
# ------------------------------------------------------------
# Type              | Convention       | Example
# ------------------|------------------|----------------------
# Variable          | snake_case       | student_name
# Constant          | UPPER_SNAKE_CASE | MAX_LIMIT
# Function          | snake_case       | calculate_tax()
# Class             | PascalCase       | BankAccount
# Protected member  | _single_prefix   | _helper()
# Private member    | __double_prefix  | __secret()
# Magic/Dunder      | __both_sides__   | __init__()
# Module alias      | short lowercase  | import numpy as np
