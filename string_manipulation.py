def modify_string(input_str):
    '''
    Modify a given alphanumeric string by repeating each alphabetic character 
    based on the corresponding numeric digit count.

    Parameters:
    input_str (str): The input alphanumeric string to be modified.

    Returns:
    str: The modified string where each alphabetic character is repeated 
         based on the corresponding numeric digit count.

    Example:
    If input_str is 'a2b3c1', the function returns 'aabbbccc'.
    '''
    # Create lists of alphabetic characters and numeric digits from the input string
    char_list = [val for val in input_str if val.isalpha()]
    num_list = [int(val) for val in input_str if val.isdigit()]

    # Create a dictionary mapping each alphabetic character to its corresponding numeric digit count
    count_dict = dict(zip(char_list, num_list))

    # Construct the modified string by repeating each alphabetic character based on its count
    return ''.join(k * v for k, v in count_dict.items())

# Prompt the user to enter an alphanumeric string to be modified
sample_string = input('Enter an alphanumeric string to modify here: ')

# Print the modified string
print(f'Modified string is: {modify_string(sample_string)}')

