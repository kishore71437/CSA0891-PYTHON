# Example sorted array
sorted_array = [0,0,00,0,0]

# Initialize result list
result = []

# Iterate through the sorted array
i = 0
while i < len(sorted_array):
    # Check if the current element is a duplicate
    if (i > 0 and sorted_array[i] == sorted_array[i - 1]) or (i < len(sorted_array) - 1 and sorted_array[i] == sorted_array[i + 1]):
        # Skip all occurrences of this element
        while i < len(sorted_array) - 1 and sorted_array[i] == sorted_array[i + 1]:
            i += 1
    else:
        # If it's not a duplicate, add it to the result
        result.append(sorted_array[i])
    i += 1

# Print the result
print(result)  # Output: [1, 3, 5]