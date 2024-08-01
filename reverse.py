number_str = input("Enter the number: ")
reversed_number_str = number_str[::-1]
if number_str == reversed_number_str:
    print("The number is already a mirror number.")
else:
    print("To make the number a mirror number, reverse it:", reversed_number_str)
