def play_with_string(input_str):
    '''
    Modify a given string by appending the count of each character followed by the character itself.

    Parameters:
    input_str (str): The input string to be modified.

    Returns:
    str: The modified string where each character is followed by its count.

    Example:
    If input_str is 'hello', the function returns '1h1e2l1o'.
    '''
    # Convert the input string into a list of characters
    char_list = list(input_str)
    
    # Create a dictionary mapping each character to its count in the input string
    char_dict = {val: char_list.count(val) for val in char_list}

    # Construct the modified string by appending the count of each character followed by the character itself
    return ''.join(str(v) + k for k, v in char_dict.items())

# Prompt the user to enter a string to be modified
sample_string = input('Enter an alphanumeric string to modify here: ')

# Print the modified string
print(f'Modified string is: {play_with_string(sample_string)}')
