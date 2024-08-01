number = int(input("Enter a number: "))
lsb = number & 1
msb = 0
bit_position = 0
temp_number = number
while temp_number > 0:
    msb = 1
    temp_number >>= 1
    bit_position += 1
msb <<= (bit_position - 1)
print(f"The Least Significant Bit (LSB) of {number} is: {lsb}")
print(f"The Most Significant Bit (MSB) of {number} is: {msb}")
