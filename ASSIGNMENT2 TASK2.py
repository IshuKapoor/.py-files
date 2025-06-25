# Sum of Integers from 1 to 50 Using a For Loop

total_sum = 0

for i in range(1, 51):
    total_sum += i

print(f"The sum of integers from 1 to 50 is: {total_sum}")

print("\n" + "="*40)
print("DETAILED VERSION WITH STEP-BY-STEP")
print("="*40)

total_sum_detailed = 0
numbers_added = []

for i in range(1, 51):
    total_sum_detailed += i
    numbers_added.append(i)
    
    if i % 10 == 0:
        print(f"Sum after adding numbers 1 to {i}: {total_sum_detailed}")

print(f"\nFinal sum: {total_sum_detailed}")

print("\n" + "="*40)
print("VERIFICATION USING MATHEMATICAL FORMULA")
print("="*40)

n = 50
formula_result = n * (n + 1) // 2
print(f"Using formula n(n+1)/2 where n=50:")
print(f"Result: {n} × {n+1} ÷ 2 = {formula_result}")
print(f"Loop result matches formula: {total_sum == formula_result}")

print("\n" + "="*40)
print("ALTERNATIVE LOOP IMPLEMENTATIONS")
print("="*40)

# Alternative 1: Using while loop #
print("1. Using while loop:")
sum_while = 0
i = 1
while i <= 50:
    sum_while += i
    i += 1
print(f"   Sum using while loop: {sum_while}")

# Alternative 2: Using sum() with range() #
print("2. Using sum() with range():")
sum_builtin = sum(range(1, 51))
print(f"   Sum using built-in sum(): {sum_builtin}")

# Alternative 3: Using list comprehension #
print("3. Using list comprehension:")
sum_list_comp = sum([i for i in range(1, 51)])
print(f"   Sum using list comprehension: {sum_list_comp}")