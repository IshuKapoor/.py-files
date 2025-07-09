# REUSE IN LOOPS AND COMDITIONS #
def is_even(n):

    return n % 2 == 0

# Check for multiple numbers #
for i in range(1, 11):
    if is_even(i):
        print(f"{i} is even")
