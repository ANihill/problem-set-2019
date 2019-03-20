# Adam Nihill, 2019-03-20
# Program that takes a user input string and outputs every second word

# Set string1 equal to the user input
string1 = (input ("Please enter sentence: "))

# Used slice notation to create a list omitting every second word 
# https://stackoverflow.com/a/509295
second_word = string1.split()[::2]

# Joined the list to create a string to output 
string2 = ' '.join(second_word)

print(string2)