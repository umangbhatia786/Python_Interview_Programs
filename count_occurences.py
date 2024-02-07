def count_occurences(input_list, input_number):
    '''
    Count the number of occurrences of a given number in a list.

    Parameters:
    input_list (list): The list of numbers.
    input_number (int): The number whose occurrences are to be counted.

    Returns:
    int: The count of occurrences of the given number in the list.
    '''
    count = 0
    for i in range(len(input_list)):
        if input_list[i] == input_number:
            count += 1
    return count

# Prompt the user to input the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the array with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Prompt the user to input the number whose count is required
num = int(input('Enter the number whose count is required: '))

# Print the count of the input number in the given array
print(f'The count of {num} in given array is {count_occurences(input_arr, num)}')
