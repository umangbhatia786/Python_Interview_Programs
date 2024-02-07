def reverse_every_second_word_internally(input_string):
    '''
    Reverse every second word internally in a given string.

    Parameters:
    input_string (str): The input string to be processed.

    Returns:
    str: The input string with every second word reversed internally.
    '''
    # Split the input string into a list of words
    word_list = input_string.split(" ")
    new_word_list = list()

    # Iterate through the list of words
    for i in range(len(word_list)):
        # Check if the word is at an even index
        if i % 2 == 0:
            new_word_list.append(word_list[i])  # Append the word as it is
        else:
            new_word_list.append(word_list[i][::-1])  # Reverse the word and append

    # Join the modified list of words back into a string
    return ' '.join(new_word_list)

# Prompt the user to enter a string to reverse every second word internally
sample_string = input('Enter a string you wish to reverse internally: ')

# Print the internally reversed string with every second word reversed
print(f'Internally reversed string is: {reverse_every_second_word_internally(sample_string)}')
