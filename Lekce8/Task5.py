def count_words_starting_with(input_file_path, char):
    # Open the input text file and read its contents
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into words
    words = content.split()

    # Count the words that start with the specified character
    count = sum(word.startswith(char) for word in words)

    return count

# Define the input file path
input_file_path = 'data/text.txt'

# Define the character
char = 'd'

# Call the function to count the words
word_count = count_words_starting_with(input_file_path, char)

print("Počet slov začínajících na znak '{}': {}".format(char, word_count))
