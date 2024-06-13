def extract_long_words(input_file_path, output_file_path, min_length=7):
    # Open the input text file and read its contents
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into words
    words = content.split()

    # Filter words that have at least the specified number of letters
    long_words = [word for word in words if len(word) >= min_length]

    # Write these words to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for word in long_words:
            output_file.write(word + '\n')


# Define the input and output file paths
input_file_path = 'data/text.txt'
output_file_path = 'data/long_words.txt'

# Call the function to process the file
extract_long_words(input_file_path, output_file_path)

output_file_path
