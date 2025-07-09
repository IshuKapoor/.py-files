# MODULAR DESIGN #
def get_input():
    return int(input("enter a number: "))

def display_square():
    num=get_input()
    print(" Square is: ", num**2)

    display_square()