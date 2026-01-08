# --------------------
# Print Debugger
# --------------------

x = 42
print("DEBUG: x =", x)  # track variable values

# --------------------
# Type Debugger
# --------------------

x = "42"
print(type(x))  # <class 'str'>
x = int(x)

# --------------------
# Assertions Debugger
# --------------------

my_list = []
assert len(my_list) > 0, "List cannot be empty!"

# --------------------
# Built-In Debugger
# --------------------

import pdb

x = 10
y = 0
pdb.set_trace()  # code stops here, inspect variables
z = x / y  # you can step through this line

# --------------------
# Try/Except Runtime Debugger
# --------------------

try:
    z = x / y
except ZeroDivisionError:
    print("Caught division by zero!")