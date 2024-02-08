def titalize(input_str):
    """
    Capitalizes the first letter of each word in a given string.

    Args:
    - input_str (str): The input string to be titalized.

    Returns:
    - titalized_str (str): The titalized string with the first letter of each word capitalized.
    """

    # Split the input string into a list of words
    str_list = input_str.split(' ')

    # Capitalize the first letter of each word and join them back into a string
    titalized_str = ' '.join(word[0].upper() + word[1:] for word in str_list)

    return titalized_str


# Get a sample string from the user to titalize
sample_string = input('Enter a sentence to titalize: ')

# Print a header to indicate the titalized string is about to be displayed
print('******* Titalized string is as below **********')

# Call the titalize function to capitalize the first letter of each word and print the result
print(titalize(sample_string))
