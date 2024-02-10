def reverse_vowels(input_str):
    """
    Reverses the vowels in a given string.

    This function takes a string as input and returns a new string where all the vowels (a, e, i, o, u) 
    in the input string are reversed. The case of the vowels is preserved, and non-vowel characters remain 
    in their original positions.

    Parameters:
    - input_str (str): The string whose vowels are to be reversed.

    Returns:
    - str: A new string with the vowels reversed in order.

    Example:
    >>> reverse_vowels("hello world")
    'hollo werld'
    """
    # Convert the input string into a list of characters for easy manipulation.
    char_list = list(input_str)
    # Lists to keep track of vowels and their indices.
    vowel_list = list()
    index_list = list()
    # List to construct the new string with reversed vowels.
    new_char_list = list()

    # Iterate over the characters, identifying vowels and their positions.
    for i in range(len(char_list)):
        if char_list[i].lower() in 'aeiou':
            vowel_list.append(char_list[i])
            index_list.append(i)
        else:
            new_char_list.append(char_list[i])

    # Reverse the list of vowels.
    rev_vowel_list = vowel_list[::-1]

    # Insert the reversed vowels back into their original positions.
    for i in range(len(rev_vowel_list)):
        new_char_list.insert(index_list[i], rev_vowel_list[i])

    # Join the list into a string and return.
    return ''.join(new_char_list)


# Example usage
sample_string = input('Enter a word to modify: ')
# Print the result of the function call.
print(f'String with reversed vowels => {reverse_vowels(sample_string)}')
