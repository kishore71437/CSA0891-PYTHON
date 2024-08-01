num = int(input("Enter a number: "))
num_str = str(num)
if len(num_str) % 2 == 0: 
    half_len = len(num_str) // 2
    first_half = int(num_str[:half_len])
    second_half = int(num_str[half_len:])
    
    if (first_half + second_half) ** 2 == num:
        print("The number is a Tech number.")
    else:
        print("The number is not a Tech number.")
else:
    print("The number is not a Tech number because it does not have an even number of digits.")