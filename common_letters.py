def find_common_letters(input_str1, input_str2):
    '''
    Find common letters between two strings and return a dictionary
    with each common letter and its count in the second string.

    Parameters:
    input_str1 (str): The first input string.
    input_str2 (str): The second input string.

    Returns:
    dict: A dictionary containing common letters from input_str2
          and their count in input_str2, if they exist in input_str1.
    '''
    # Create lists of unique characters from input_str1 and input_str2
    str_list_1 = list(set(input_str1))
    str_list_2 = list(set(input_str2))

    # Create a dictionary comprehension to count common letters
    return {letter: input_str2.count(letter) for letter in input_str2 if letter in input_str1}

# Prompt the user to enter the two strings
string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')

# Find and print the common letters and their counts in string2
print(find_common_letters(string1, string2))
