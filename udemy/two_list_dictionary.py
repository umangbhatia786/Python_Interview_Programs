def create_list(length, data_type=int):
    """
    Create a list of specified length by taking user input for each element.

    Args:
    - length (int): The length of the list to create.
    - data_type (type, optional): The data type of the elements. Defaults to int.

    Returns:
    - list: The created list filled with user input values.

    Example:
    >>> create_list(3, int)
    Enter value for index 0: 1
    Enter value for index 1: 2
    Enter value for index 2: 3
    [1, 2, 3]
    """
    input_arr = list()
    for i in range(0, length):
        val = data_type(input(f'Enter value for index {i}: '))
        input_arr.append(val)
    return input_arr

def two_list_dictionary(list1, list2):
    """
    Create a dictionary from two lists, with elements of list1 as keys and elements of list2 as values.
    If the length of list1 is greater than list2, remaining keys in the dictionary will have None as values.

    Args:
    - list1 (list): The list of keys for the dictionary.
    - list2 (list): The list of values for the dictionary.

    Returns:
    - dict: The dictionary created from list1 and list2.

    Example:
    >>> two_list_dictionary(['a', 'b', 'c'], [1, 2])
    {'a': 1, 'b': 2, 'c': None}
    """
    if len(list1) == len(list2) or len(list1) < len(list2):
        return dict(zip(list1, list2))
    else:
        my_dict = {}
        for i in range(len(list1)):
            if i < len(list2):
                my_dict[list1[i]] = list2[i]
            else:
                my_dict[list1[i]] = None
        return my_dict

# Prompt the user to enter the length and data type for the first list
length1 = int(input('Enter length of array1 you wish to create: '))
input_arr1 = create_list(length1, str)

# Prompt the user to enter the length for the second list
length2 = int(input('Enter length of array2 you wish to create: '))
input_arr2 = create_list(length2)

# Create a dictionary from the two lists
output_dict = two_list_dictionary(input_arr1, input_arr2)

# Print the created dictionary with key-value pairs
print('********** Created a dictionary with below key value pairs **********')
for k, v in output_dict.items():
    print(f'{k} => {v}')
