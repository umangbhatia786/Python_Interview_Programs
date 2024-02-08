def read_contents_from_a_file(input_file_path):
    '''
    Read contents from a file and return them as a list of lines.

    Parameters:
    input_file_path (str): The path to the input file.

    Returns:
    list: A list containing the contents of the file as lines.

    Example:
    If 'file1.txt' contains:
    ```
    Line 1
    Line 2
    Line 3
    ```
    The function returns ['Line 1\n', 'Line 2\n', 'Line 3\n'].
    '''
    # Open the input file and read its contents into a list of lines
    with open(input_file_path, 'r') as f:
        content_list = f.readlines()

    return content_list

def write_content_to_a_file(output_file_path, content_by_lines):
    '''
    Write content to a file from a list of lines.

    Parameters:
    output_file_path (str): The path to the output file.
    content_by_lines (list): A list containing the content to be written to the file as lines.

    Returns:
    None

    Example:
    If content_by_lines is ['Line 1\n', 'Line 2\n', 'Line 3\n'], 
    the function writes this content to the file specified by output_file_path.
    '''
    # Open the output file and write the content from the list of lines
    with open(output_file_path, 'w') as myFile:
        myFile.writelines(content_by_lines)


# Read contents from 'file1.txt'
content = read_contents_from_a_file('file_handling/file1.txt')

# Write the contents to 'file2.txt'
write_content_to_a_file('file_handling/file2.txt', content)
