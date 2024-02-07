def find_max(input_list):
    '''
    Find the maximum value in the given list.

    Parameters:
    input_list (list): The list containing numeric elements.

    Returns:
    int: The maximum value in the list.
    '''
    max_val = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_val:
            max_val = input_list[i]

    return max_val

def find_min(input_list):
    '''
    Find the minimum value in the given list.

    Parameters:
    input_list (list): The list containing numeric elements.

    Returns:
    int: The minimum value in the list.
    '''
    min_val = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] < min_val:
            min_val = input_list[i]

    return min_val

# Prompt the user to input the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the array with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Find and display the maximum and minimum values in the array
print(f'Maximum value in the array is: {find_max(input_arr)}')
print(f'Minimum value in the array is: {find_min(input_arr)}')
