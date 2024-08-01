def find_repeated_letters(word):
    letter_count = {}
    repeated_letters = []

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter, count in letter_count.items():
        if count > 1:
            repeated_letters.append(letter)
    
    print(f"Number of repeated letters = {len(repeated_letters)}")
    if repeated_letters:
        print("Repeated letter(s) =", ' '.join(repeated_letters))

# Sample Input
word = input("Enter the word: ")

# Sample Output
find_repeated_letters(word)