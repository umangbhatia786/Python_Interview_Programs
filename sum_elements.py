def sum_elements(input_arr):
    '''
    Calculate the sum of elements in a given array.

    Parameters:
    input_arr (list): The input array containing numeric elements.

    Returns:
    int: The sum of elements in the input array.
    '''
    sum = 0
    for val in input_arr:
        sum += val
    return sum

# Prompt the user to input the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the array with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Calculate and display the sum of elements in the array
print(f'Sum of elements of given array is {sum_elements(input_arr)}')
