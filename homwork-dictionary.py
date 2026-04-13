# 1. Create the dictionary
test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

# 2. Print it so the user can see it
print("Test Dictionary:", test_dict)

# 3. Ask the user what number (value) they are looking for
# We use int() because the values in our dictionary are numbers
check_value = int(input("Enter the value to check its frequency: "))

# 4. Set up a counter starting at zero
frequency = 0

# 5. The "Counting" Loop
# We use .values() because we only care about the numbers, not the words
for v in test_dict.values():
    if v == check_value:
        frequency = frequency + 1

# 6. Show the final count
print(f"The value {check_value} appears {frequency} times.")
