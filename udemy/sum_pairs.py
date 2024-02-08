def sum_pairs(input_list, input_num):
    """
    Finds the first pair of numbers in a given list that sum up to a specified number.

    Args:
    - input_list (list): A list of integers to search for pairs.
    - input_num (int): The target number to find pairs that sum up to.

    Returns:
    - pair_list (list): The first pair of numbers that sum up to the specified number.
    """

    pair_list = list()  # Initialize an empty list to store pairs

    # Iterate through each element in the input_list
    for i in range(len(input_list)):
        # Iterate through the subsequent elements to find pairs
        for j in range(i+1, len(input_list)):
            # Check if the sum of the current pair equals the input_num
            if input_list[i] + input_list[j] == input_num:
                # If so, add the pair to the pair_list
                pair_list.append([input_list[i], input_list[j]])

    # Return the first pair found, if any
    return pair_list[0]

# Get the length of the array from user input
length = int(input('Enter length of array you wish to create: '))

input_arr = list()  # Initialize an empty list to store user inputs

# Prompt the user to enter values for each index in the array
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)  # Append each user input to the input_arr list

# Get the number to check for pairs from user input
sample_num = int(input('Enter the number you wish to check: '))

# Find the first pair in the input array that sums up to the specified number
first_pair = sum_pairs(input_arr, sample_num)

# Check if any pair was found
if len(first_pair) == 0:
    # If no pair was found, inform the user
    print(f'There are no pairs in {input_arr} that sum up to {sample_num}')
else:
    # If a pair was found, display the pair to the user
    print(f'The first pair in {input_arr} that sums up to {sample_num} is {first_pair}')
