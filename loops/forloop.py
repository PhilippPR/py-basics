""" 
A for loop can be used to iterate over a list.

The loop repeats for each item in the list.

Example:
"""

Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for letter in Alphabet:
    print(letter)


"""
A for loop can work with index numbers.
Example:
"""

for letter in Alphabet[2:12]: # Alphabet[2:12] returns a list of the letters from index 2 to index 12-1.
    print(letter)


"""
Working with range()
Example:
"""

for i in range(5): # range(5) returns a list of numbers from 0 to 4. > an index starts at 0.
    # This loop will get Repeat 5 times.
    print(i) # This will print the number of the index the loop is at the moment.