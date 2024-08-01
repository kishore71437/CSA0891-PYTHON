binary1=input("Enter the value of b1:")
binary2=input("Enter the value of b2:")
binary3=input("Enter the value of b3:")
decimal1=int(binary1,2)
decimal2=int(binary2,2)
decimal3=int(binary3,2)
if decimal1>=decimal2 and decimal1>=decimal3:
    greatest_number=binary1
elif decimal2>=decimal1 and decimal2>=decimal3:
    greatest_number= binary2
else:
    greatest_number=binary3
    print(f"the greatest binary number : {greatest_number}")