def find_character_in_string(string, char):
    for index in range(len(string)):
        if string[index] == char:
            print(f"{char} is found in string at index: {index}")
            return
    print(f"{char} is not found in the string")

# Sample Input
string = input("Enter the string: ")
char = input("Enter the character to be searched: ")

# Sample Output
find_character_in_string(string, char)