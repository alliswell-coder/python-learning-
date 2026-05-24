# ============================================================
# PYTHON CASE STYLES - Complete Overview
# ============================================================
# Python follows PEP 8 (Python Enhancement Proposal 8) as the
# official style guide. Different case styles are used for
# different types of identifiers.
# ============================================================


# ------------------------------------------------------------
# 1. snake_case  (most common in Python)
# ------------------------------------------------------------
# - All letters lowercase
# - Words separated by underscores
# - Used for: variables, functions, method names, module names

# Variables
first_name = "Alice"
last_name = "Smith"
total_price = 99.99
is_logged_in = True
max_retry_count = 3
user_email_address = "alice@example.com"

# Functions
def get_user_name():
    return "Alice"

def calculate_total_price(price, tax):
    return price + tax

def send_email_notification(recipient, message):
    pass

def is_valid_email(email):
    return "@" in email

def fetch_data_from_api(url, timeout=30):
    pass


# ------------------------------------------------------------
# 2. UPPER_SNAKE_CASE / SCREAMING_SNAKE_CASE
# ------------------------------------------------------------
# - All letters uppercase
# - Words separated by underscores
# - Used for: constants (values that never change)

PI = 3.14159265358979
GRAVITY = 9.8
MAX_CONNECTIONS = 100
MIN_PASSWORD_LENGTH = 8
DEFAULT_TIMEOUT = 30
BASE_API_URL = "https://api.example.com"
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
MAX_FILE_SIZE_MB = 50
APP_VERSION = "1.0.0"
DEBUG_MODE = False
TAX_RATE = 0.18
DAYS_IN_A_WEEK = 7
HTTP_STATUS_OK = 200
HTTP_STATUS_NOT_FOUND = 404


# ------------------------------------------------------------
# 3. PascalCase / UpperCamelCase
# ------------------------------------------------------------
# - Each word starts with an uppercase letter
# - No separators between words
# - Used for: class names, exception names

class UserAccount:
    pass

class BankTransaction:
    pass

class ProductInventory:
    pass

class EmailNotificationService:
    pass

class DatabaseConnectionManager:
    pass

class HttpRequestHandler:
    pass

# Exception classes (also PascalCase)
class InvalidEmailError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass

class PaymentFailedException(Exception):
    pass

class UserNotFoundException(Exception):
    pass


# ------------------------------------------------------------
# 4. camelCase / lowerCamelCase
# ------------------------------------------------------------
# - First word lowercase, subsequent words capitalized
# - NOT recommended in Python (used in Java/JavaScript)
# - Sometimes seen in: JSON keys, external API data, legacy code

# Not Pythonic — avoid in your own code:
firstName = "Bob"           # should be: first_name
lastName = "Jones"          # should be: last_name
isActive = True             # should be: is_active
totalAmount = 250.00        # should be: total_amount

# Common in JSON / API response data (when parsing external data):
api_response = {
    "userId": 101,
    "firstName": "Alice",
    "isActive": True,
    "accountBalance": 5000.00
}


# ------------------------------------------------------------
# 5. _single_leading_underscore
# ------------------------------------------------------------
# - Single underscore before the name
# - Convention for "internal / protected" use
# - Not enforced by Python — just a hint to developers

class MyService:
    def __init__(self):
        self._connection = None       # protected instance variable
        self._retry_count = 0         # protected instance variable

    def _connect(self):               # protected method
        pass

    def _validate_input(self, data):  # protected helper method
        pass

# Module-level internal variables
_internal_cache = {}
_default_config = {"debug": False}


# ------------------------------------------------------------
# 6. __double_leading_underscore (Name Mangling)
# ------------------------------------------------------------
# - Double underscore before the name
# - Python internally renames it to _ClassName__name
# - Used for: truly private attributes to avoid subclass conflicts

class SecureAccount:
    def __init__(self, owner, pin):
        self.__pin = pin              # private — name-mangled to _SecureAccount__pin
        self.__balance = 0            # private — name-mangled to _SecureAccount__balance
        self.owner = owner            # public

    def __validate_pin(self, pin):   # private method
        return self.__pin == pin

    def get_balance(self, pin):
        if self.__validate_pin(pin):
            return self.__balance
        return "Unauthorized"


# ------------------------------------------------------------
# 7. __dunder__ / Magic Methods (Double underscore on BOTH sides)
# ------------------------------------------------------------
# - Double underscore before AND after the name
# - Built-in special methods used by Python internally
# - Never create your own __dunder__ names

class Book:
    def __init__(self, title, pages):   # called on object creation
        self.title = title
        self.pages = pages

    def __str__(self):                  # called by str() and print()
        return f"Book: {self.title}"

    def __repr__(self):                 # called by repr()
        return f"Book(title='{self.title}', pages={self.pages})"

    def __len__(self):                  # called by len()
        return self.pages

    def __eq__(self, other):            # called by ==
        return self.title == other.title

    def __lt__(self, other):            # called by <
        return self.pages < other.pages

    def __add__(self, other):           # called by +
        return Book(self.title + " & " + other.title, self.pages + other.pages)

    def __contains__(self, item):       # called by 'in'
        return item in self.title

    def __getitem__(self, index):       # called by []
        return self.title[index]

    def __del__(self):                  # called on object deletion
        pass


# ------------------------------------------------------------
# 8. MIXEDCASE (rare — avoid in Python)
# ------------------------------------------------------------
# - Mix of uppercase and lowercase without a consistent pattern
# - Not recommended — only seen in very old or legacy Python code

# Old style (avoid):
myVariable = 10     # inconsistent
MyFunction = None   # confusing — looks like a class


# ------------------------------------------------------------
# 9. CASE STYLE QUICK REFERENCE SUMMARY
# ------------------------------------------------------------

# Style             | Convention           | Used For
# ------------------|----------------------|--------------------------------
# snake_case        | all_lowercase_words  | variables, functions, methods, modules
# UPPER_SNAKE_CASE  | ALL_UPPERCASE_WORDS  | constants
# PascalCase        | CapitalizeEachWord   | classes, exceptions
# camelCase         | firstLowerThenCaps   | NOT Pythonic (avoid)
# _protected        | _single_underscore   | internal/protected members
# __private         | __double_underscore  | private (name-mangled) members
# __dunder__        | __both_sides__       | magic/special methods


# ------------------------------------------------------------
# 10. REAL-WORLD EXAMPLE combining all case styles
# ------------------------------------------------------------

MAX_LOGIN_ATTEMPTS = 5          # UPPER_SNAKE_CASE constant


class UserAuthService:          # PascalCase class
    _instance = None            # _protected class variable

    def __init__(self, db_host, db_port):   # snake_case params
        self.db_host = db_host              # snake_case instance variable
        self.db_port = db_port
        self.__secret_key = "s3cr3t"        # __private instance variable
        self._attempt_count = 0             # _protected instance variable

    def __str__(self):                      # __dunder__ magic method
        return f"UserAuthService({self.db_host}:{self.db_port})"

    def _hash_password(self, password):     # _protected helper method
        return hash(password)

    def __check_attempt_limit(self):        # __private method
        return self._attempt_count < MAX_LOGIN_ATTEMPTS

    def authenticate_user(self, username, password):  # snake_case public method
        if not self.__check_attempt_limit():
            raise PaymentFailedException("Too many attempts")
        hashed = self._hash_password(password)
        self._attempt_count += 1
        return hashed is not None


auth_service = UserAuthService("localhost", 5432)   # snake_case variable
print(auth_service)
