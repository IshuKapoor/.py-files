# Even or Odd Checker Program

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

print("\n" + "="*30)
print("DETAILED VERSION")
print("="*30)

number2 = int(input("Enter another integer: "))

if number2 % 2 == 0:
    print(f"{number2} is even because {number2} ÷ 2 = {number2//2} with remainder {number2%2}")
else:
    print(f"{number2} is odd because {number2} ÷ 2 = {number2//2} with remainder {number2%2}")

if number2 == 0:
    print("Note: Zero is considered an even number.")
    