def find_factors(input_num):
    """
    Finds the factors of a given integer.

    Args:
    - input_num (int): The integer for which factors are to be found.

    Returns:
    - factor_list (list): A list of all the factors of the input number.
    """

    # Initialize an empty list to store factors
    factor_list = []

    # Generate factors by iterating through numbers from 1 to input_num
    # Check if each number is a factor of input_num
    # If it is, add it to the factor_list
    return [num for num in range(1, input_num + 1) if input_num % num == 0]

# Get user input for the number to find factors for
sample_num = int(input('Input a number for which you wish to find factors: '))

# Call the find_factors function to get the factors of the sample_num
factors_list = find_factors(sample_num)

# Print the factors of the sample_num
print(f'Factors for {sample_num} are {factors_list}')
