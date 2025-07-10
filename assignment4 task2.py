# Step 1: Take user input and write to file
user_input = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
additional_input = input("Enter more text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
