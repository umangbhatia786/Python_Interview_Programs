def reverse_words_in_string(input_str):
    '''
    Reverse the order of words in a given string.

    Parameters:
    input_str (str): The input string to be reversed.

    Returns:
    str: The reversed string with words in reverse order.
    '''
    # Split the input string into a list of words based on space separator
    word_list = input_str.split(" ")
    
    # Join the words in reverse order using space separator
    reversed_string = ' '.join(word for word in word_list[::-1])
    
    return reversed_string

# Prompt the user to input a sentence to be reversed
sample_string = input('Enter a sentence to reverse: ')

# Print the reversed string with words in reverse order
print('******** Reversed String is as below *********')
print(reverse_words_in_string(sample_string))
