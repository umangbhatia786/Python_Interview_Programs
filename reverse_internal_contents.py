def reverse_words_internally(input_string):
    '''
    Reverse each word internally in a given string.

    Parameters:
    input_string (str): The input string to be processed.

    Returns:
    str: The input string with each word reversed internally.
    '''
    # Split the input string into a list of words
    words_list = input_string.split(" ")
    
    # Reverse each word internally and join them back into a string
    reversed_string = ' '.join(word[::-1] for word in words_list)
    
    return reversed_string

# Prompt the user to enter a string to reverse internally
sample_string = input('Enter a string you wish to reverse internally: ')

# Print the internally reversed string
print(f'Internally reversed string is: {reverse_words_internally(sample_string)}')
