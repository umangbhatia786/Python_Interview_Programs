def get_vowel_count(input_string):
    '''
    Count the occurrences of vowels in a given string.

    Parameters:
    input_string (str): The input string to count vowels in.

    Returns:
    dict: A dictionary containing the count of each vowel in the input string.

    Example:
    If input_string is 'Hello World', the function returns {'e': 1, 'o': 2}.
    '''
    # Convert the input string to lowercase to make it case-insensitive
    lower_string = input_string.lower()

    # Count the occurrences of each vowel in the lowercased string
    return {val: lower_string.count(val) for val in lower_string if val in 'aeiou'}

# Prompt the user to enter a sample string
sample_string = input('Enter your sample string here: ')

# Get the vowel count dictionary for the sample string
vowel_count_dict = get_vowel_count(sample_string)

# Check if there are any vowels in the sample string
if len(vowel_count_dict) == 0:
    print('There were no vowels in the given string')
else:
    # Print the vowel count
    print('******* The vowel count is as below ***********')
    for k, v in vowel_count_dict.items():
        print(f'{k} --> {v}')