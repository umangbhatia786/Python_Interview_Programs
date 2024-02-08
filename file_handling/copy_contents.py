def read_contents_from_a_file(input_file_path):

    with open(input_file_path, 'r') as f:
        content_list = f.readlines()

    return content_list

def write_content_to_a_file(output_file_path, content_by_lines):

    with open(output_file_path, 'w') as myFile:
        myFile.writelines(content_by_lines)


content = read_contents_from_a_file('file_handling/file1.txt')
write_content_to_a_file('file_handling/file2.txt', content)