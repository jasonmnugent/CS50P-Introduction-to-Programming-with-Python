# Ask the user to input a string
input_str = input("Enter a string: ")

# Split the input string into words ... splt() will split input strings into words
words = input_str.split()

# Join the words together with 3 dots in between ... join() will join words together, and
# the "..." will become the separator
output_str = "...".join(words)

# Print the output string
print(output_str)