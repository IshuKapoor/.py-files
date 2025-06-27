import math

# Ask the user to input a number
num = float(input("Enter a number: "))

# Calculate square root
square_root = math.sqrt(num)

# Calculate natural logarithm (base e)
# (Check if the number is positive for log)
if num > 0:
    natural_log = math.log(num)
else:
    natural_log = "Undefined (log not defined for zero or negative numbers)"

# Calculate sine (in radians)
sine_value = math.sin(num)

# Display the results
print("\nResults:")
print("Square root:", square_root)
print("Natural logarithm (ln):", natural_log)
print("Sine (in radians):", sine_value)
