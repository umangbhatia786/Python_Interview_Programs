import math

def check_armstrong(input_number):
    '''
    Check if a given number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised 
    to the power of the number of digits in the number.

    Parameters:
    input_number (int): The number to be checked.

    Returns:
    bool: True if the number is an Armstrong number, False otherwise.

    Example:
    If input_number is 153, the function returns True because 1^3 + 5^3 + 3^3 = 153.

    '''
    # Convert the input number into a list of its digits
    number_list = list(str(input_number))

    # Calculate the sum of each digit raised to the power of the number of digits
    sum = 0
    for val in number_list:
        sum += math.pow(int(val), len(number_list))

    # Check if the sum is equal to the original number
    return sum == input_number

# Prompt the user to enter a number to be checked for Armstrong property
sample_number = int(input('Enter your number here: '))

# Check if the number is an Armstrong number and print the result
if check_armstrong(sample_number):
    print(f'{sample_number} is an Armstrong Number')
else:
    print(f'{sample_number} is not an Armstrong Number')
