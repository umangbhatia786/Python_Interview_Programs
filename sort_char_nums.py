def sort_char_nums(input_string):
    '''
    Sort alphabetic characters and numeric digits in a given string and concatenate them.

    Parameters:
    input_string (str): The input string containing alphabetic characters and numeric digits.

    Returns:
    str: The sorted string with alphabetic characters and numeric digits concatenated.

    Example:
    If input_string is 'a2b1c3', the function returns 'abc123'.
    '''
    # Create lists of alphabetic characters and numeric digits from the input string
    chars_list = [val for val in input_string if val.isalpha()]
    num_list = [val for val in input_string if val.isdigit()]

    # Sort the lists of alphabetic characters and numeric digits
    sorted_chars_list = sorted(chars_list)
    sorted_num_list = sorted(num_list)

    # Concatenate the sorted lists and return the sorted string
    return ' '.join(sorted_chars_list + sorted_num_list)


# Prompt the user to enter an alphanumeric string to be sorted
sample_string = input('Enter an alphanumeric string to sort here: ')

# Print the sorted string
print(f'Sorted string is: {sort_char_nums(sample_string)}')
