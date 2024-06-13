def add_asterisks(input_file_path, output_file_path):
    # Open the input text file and read its lines
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Find the last line without a comma
    last_non_comma_index = -1
    for i, line in enumerate(lines):
        if ',' not in line:
            last_non_comma_index = i

    # If no lines without commas are found, append the asterisks at the end
    if last_non_comma_index == -1:
        lines.append('************\n')
    else:
        # Insert the asterisks after the last non-comma line
        lines.insert(last_non_comma_index + 1, '************\n')

    # Write the modified lines to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            output_file.write(line)

# Define the input and output file paths
input_file_path = 'data/text.txt'
output_file_path = 'data/modified_text.txt'

# Call the function to process the file
add_asterisks(input_file_path, output_file_path)

output_file_path
