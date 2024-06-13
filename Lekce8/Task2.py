def copy_lines(input_file_path, output_file_path):
    # Open the input text file and read its lines
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Write these lines to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            output_file.write(line)

# Define the input and output file paths
input_file_path = 'data/text.txt'
output_file_path = 'data/copied_lines.txt'

# Call the function to copy lines from the input file to the output file
copy_lines(input_file_path, output_file_path)

output_file_path
