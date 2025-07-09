# CALCULATOR FUNCTIONS #
def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    if y == 0:
        return " cannot divide by zero "
    return x/y
# Reuse these functions #
print(add(5, 3))         # 8
print(subtract(10, 4))   # 6
print(multiply(2, 7))    # 14
print(divide(8, 2))      # 4.0