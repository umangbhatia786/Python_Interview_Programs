def get_factorial(num):
    '''
    Calculate the factorial of a given non-negative integer.

    Parameters:
    num (int): The number for which factorial needs to be calculated.

    Returns:
    int: The factorial of the input number.

    Raises:
    ValueError: If the input number is negative.
    '''
    try:
        if num == 0:
            return 1
        elif num < 0:
            raise ValueError
        else:
            factorial = 1
            # Calculate factorial using a loop from 1 to num
            for i in range(1, num+1):
                factorial *= i
            return factorial
    except ValueError:
        print('Input number cannot be less than 0')


# Prompt the user to input a number
input_num = int(input('Enter a number: '))

# Calculate and display the factorial of the input number
print(f'Factorial of given number is {get_factorial(input_num)}')
