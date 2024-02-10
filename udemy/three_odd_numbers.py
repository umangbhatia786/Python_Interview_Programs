def three_odd_numbers(input_list):
    """
    Checks if there are three consecutive odd numbers in the input list.

    Args:
    - input_list (list): The list of integers to check.

    Returns:
    - bool: True if there are three consecutive odd numbers in the list, False otherwise.

    Example:
    >>> three_odd_numbers([1, 2, 3, 4, 5])
    True
    """
    for i in range(len(input_list) - 2):
        # Check if the sum of three consecutive numbers is odd
        if sum(input_list[i:i + 3]) % 2 != 0:
            return True
    return False

# Prompt the user to enter the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the input_arr list with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Check if the list contains three consecutive odd numbers
print(f'Is the three odd numbers check valid for the given list => {three_odd_numbers(input_arr)}')
