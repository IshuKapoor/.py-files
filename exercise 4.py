#Centered pyramid star#

rows = 5

for i in range(1, rows + 1):
    
    for space in range(rows - i):
        print(" ", end="")

    for star in range(i):
        print("*", end=" ")
    print()

for i in range(rows - 1, 0, -1):

    for space in range(rows - i):
        print(" ", end="")

    for star in range(i):
        print("*", end=" ")
    print()
