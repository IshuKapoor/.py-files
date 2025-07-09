# printing a pattern with function [code reuse] #
def print_star_pattern(rows):
    for i in range(1,rows+1):
        print('*' * i)
        print()
        # Call the function multiple times #
print_star_pattern(5)
print()  
# line break#
print_star_pattern(5)
