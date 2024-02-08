def list_check(input_list):
    '''
    Check if all elements inside a list are also lists.

    Parameters:
    input_list (list): The input list to be checked.

    Returns:
    bool: True if all elements inside the list are lists, False otherwise.

    Example:
    If input_list is [[1, 2, 3], [4, 5, 6], [7, 8, 9]], the function returns True.
    '''
    # Use map and lambda function to check if each element of input_list is a list
    return all(list(map(lambda x: type(x) == list, input_list)))

# Define a sample list
sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Check if all elements inside the list are also lists
if list_check(sample_list):
    print('All elements inside the list are also lists')
else:
    print('All elements inside the list are not lists')
