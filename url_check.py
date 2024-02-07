import re

def contains_url(input_string):
    '''
    Check if a string contains any URLs.

    Parameters:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the string contains a URL, False otherwise.
    '''
    # Define a regular expression pattern to match URLs
    url_pattern = re.compile(r'https?://\S+')
    
    # Search for the pattern in the input string
    if url_pattern.search(input_string) is not None:
        return True
    return False

# Test the function with a sample input
sample_string = input('Enter a string to check for URLs: ')
if contains_url(sample_string):
    print('String contains a URL.')
else:
    print('String does not contain a URL.')
