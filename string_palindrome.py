def check_palindrome(input_str):
    '''
    Check if a given string is a palindrome.

    Parameters:
    input_str (str): The input string to be checked for palindrome.

    Returns:
    bool: True if the input string is a palindrome, False otherwise.
    '''
    # Convert the input string to lowercase and convert it to a list of characters
    str_list = list(input_str.lower())
    
    # Check if the list is equal to its reverse
    if str_list == str_list[::-1]:
        return True
    return False

# Prompt the user to input a word for verification
word = input('Enter the word to verify: ')

# Check if the input word is a palindrome and print the result
if check_palindrome(word):
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')

