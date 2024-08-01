# Input the number as a string (assuming the number is provided as input)
number_str = input("Enter the number: ")

# Reverse the number
reversed_number_str = number_str[::-1]

# Check if the reversed number is equal to the original number
if number_str == reversed_number_str:
    print("The number is already a mirror number.")
else:
    print("To make the number a mirror number, reverse it:", reversed_number_str)
