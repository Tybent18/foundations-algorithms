# --------------------
# Array/List Bounds
# --------------------

for i in range(len(my_list)):
    print(my_list[i])

# --------------------
# Verifying Swaps in Sorting
# --------------------

print("Before swap:", arr)
arr[i], arr[j] = arr[j], arr[i]
print("After swap:", arr)

# --------------------
# Trace Recursion
# --------------------

def factorial(n):
    print("factorial called with n =", n)
    if n <= 1:
        return 1
    return n * factorial(n - 1)