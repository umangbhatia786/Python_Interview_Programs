def mode(input_list):
    """
    Finds the mode (most frequent element) in the input list.

    Args:
    - input_list (list): The list of elements to find the mode from.

    Returns:
    - int or float: The mode of the input list.

    Example:
    >>> mode([1, 2, 3, 3, 4, 4, 4])
    4
    """
    # Create a dictionary to count the occurrences of each element in the input list
    count_dict = {val: input_list.count(val) for val in input_list}

    # Find the maximum count of occurrences
    max_val = max(count_dict.values())

    # Iterate through the dictionary to find the key (element) with the maximum count
    for k, v in count_dict.items():
        if v == max_val:
            return k
    
    # If there are multiple elements with the same maximum count, return the last one found
    return k

# Prompt the user to enter the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the input_arr list with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Find the mode (element with maximum frequency) in the input list and print it
print(f'Element with max frequency is {mode(input_arr)}')
