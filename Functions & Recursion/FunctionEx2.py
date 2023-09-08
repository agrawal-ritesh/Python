def calculate_average(numbers):
    if not numbers:
        return 0  # Return 0 for an empty list to avoid division by zero
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Input the numbers from the user
numbers = []
num_values = int(input("Enter the number of values: "))

for i in range(num_values):
    value = float(input("Enter a number: "))
    numbers.append(value)

# Calculate the average using the function
average = calculate_average(numbers)

# Print the result
print("The average of the numbers is:", average)
