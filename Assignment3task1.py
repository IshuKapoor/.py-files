# Calculate Factorial Using A Python #

# Using a function and a Loop #

# Function to calculate factorial #

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calling the function with a sample number
sample_number = 5
print("Factorial of", sample_number, "is:", factorial(sample_number))

# Using a Recursion #
 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function with a sample number
sample_number = 5
print("Factorial of", sample_number, "is:", factorial(sample_number))
