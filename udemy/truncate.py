def truncate(input_str, val):
    """
    Truncates a given string to a specified length, appending '...' at the end.

    Args:
    - input_str (str): The input string to truncate.
    - val (int): The length at which to truncate the string.

    Returns:
    - str: The truncated string with '...' appended at the end.

    Raises:
    - ValueError: If the truncation length is less than 3 characters.

    Example:
    >>> truncate("Hello World", 5)
    'Hel...'

    """
    # Check if the truncation length is less than 3 characters
    if val < 3:
        # Raise a ValueError if the truncation length is less than 3 characters
        raise ValueError('Truncation must be at least 3 characters.')
    else:
        # Truncate the input string to the specified length, appending '...' at the end
        return input_str[:val - 3] + '...'


# Prompt the user to enter a word to truncate and the length of truncation
sample_string = input('Enter a word to truncate: ')
trunc_length = int(input('Enter the length of truncation: '))

# Print the truncated string by calling the truncate function with the input string and truncation length
print(f'Truncated string is => {truncate(sample_string, trunc_length)}')
