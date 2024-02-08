def remove_every_other(input_list):
    '''
    Remove every other element from a given list.

    Parameters:
    input_list (list): The input list from which every other element will be removed.

    Returns:
    list: The modified list with every other element removed.

    Example:
    If input_list is [1, 2, 3, 4, 5, 6], the function returns [1, 3, 5].
    '''
    # Use list comprehension to create a new list with every other element from the input list
    return [input_list[i] for i in range(len(input_list)) if i % 2 == 0]

# Prompt the user to input the length of the array
length = int(input('Enter length of array you wish to create: '))

# Create an empty list to store user input values
input_arr = list()

# Populate the list with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Remove every other element from the input list
modified_list = remove_every_other(input_arr)

# Print the modified list after removing every 2nd element
print('******* This after removing every 2nd element is *******')
for val in modified_list:
    print(val, end=',')
