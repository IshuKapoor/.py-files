# Function to check even or odd #
def check_even_odd(number):
    if number %2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
        # Reusing the same function
check_even_odd(4)
check_even_odd(7)
check_even_odd(10)