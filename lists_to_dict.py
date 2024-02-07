def convert_lists_to_dict(list1, list2):
    '''
    Convert two lists into a dictionary.

    Parameters:
    list1 (list): The list containing keys for the dictionary.
    list2 (list): The list containing values for the dictionary.

    Returns:
    dict: A dictionary created from the two input lists.

    Raises:
    ValueError: If the lengths of the input lists are different.
    '''
    if len(list1) != len(list2):
        raise ValueError('Length of lists should be same!')
    else:
        # Use the zip() function to combine the two lists into a dictionary
        return dict(zip(list1, list2))

# Prompt the user to input the length of the first array
length1 = int(input('Enter length of array1 you wish to create: '))
input_arr1 = list()

# Populate the array with user input values
for i in range(0, length1):
    val = input(f'Enter value for index {i}: ')
    input_arr1.append(val)

# Prompt the user to input the length of the second array
length2 = int(input('Enter length of array2 you wish to create: '))
input_arr2 = list()

# Populate the array with user input values
for i in range(0, length2):
    val = int(input(f'Enter value for index {i}: '))
    input_arr2.append(val)

# Convert the two arrays into a dictionary
output_dict = convert_lists_to_dict(input_arr1, input_arr2)

print('************ The created dictionary is as below **************')
# Print the created dictionary
for k, v in output_dict.items():
    print(f'{k} : {v}')
