def alphabetical_order(word):
    sorted_word = sorted(word)
    reverse_sorted_word = sorted(word, reverse=True)
    
    print("Alphabetical Order Normal:", ' '.join(sorted_word))
    print("Alphabetical Order Reverse:", ' '.join(reverse_sorted_word))

# Sample Input
word = input("Enter the word: ")

# Sample Output
alphabetical_order(word)