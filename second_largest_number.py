def get_second_largest_number(input_list):
    '''
    Get the second largest number from the given list using sorting.

    Parameters:
    input_list (list): The list of numbers.

    Returns:
    int: The second largest number in the list.
    '''
    sorted_list = sorted(input_list)
    return sorted_list[-2]

def get_second_largest_number_2(input_list):
    '''
    Get the second largest number from the given list using iteration.

    Parameters:
    input_list (list): The list of numbers.

    Returns:
    int: The second largest number in the list.
    '''
    max = input_list[0]
    second_max = input_list[1]

    for i in range(2,len(input_list)):
        if input_list[i] > max:
            second_max = max
            max = input_list[i]
        elif input_list[i] < max and input_list[i] > second_max:
            second_max = input_list[i]

    return second_max


# Prompt the user to input the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the array with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

# Print the second largest elements using two different methods
print(f'2nd largest element in the array is {get_second_largest_number(input_arr)}')
print(f'2nd largest element as per way second is {get_second_largest_number_2(input_arr)}')
