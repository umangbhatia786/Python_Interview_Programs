import re

def contains_special_characters(input_string):
    '''
    Check if a string contains any special characters.

    Parameters:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the string contains special characters, False otherwise.
    '''
    # Define a regular expression pattern to match special characters
    special_char_pattern = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    
    # Search for the pattern in the input string
    if special_char_pattern.search(input_string) is not None:
        return True
    return False

# Test the function with a sample input
sample_string = input('Enter a string to check for special characters: ')
if contains_special_characters(sample_string):
    print('String contains special characters.')
else:
    print('String does not contain special characters.')
