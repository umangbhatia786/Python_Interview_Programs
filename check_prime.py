def check_prime(num):
    '''
    Function to verify if a number is prime or not.

    Parameters:
    num (int): The number to be checked for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    '''
    flag = True

    # Loop through numbers from 2 to num - 1
    for val in range(2, num):
        # If num is divisible by any number in the range, it's not prime
        if num % val == 0:
            flag = False
            break

    return flag

# Prompt the user to input a number
input_num = int(input('Enter the number to verify: '))

# Check if the input number is prime and display the result
if check_prime(input_num):
    print('The given number is a Prime Number')
else:
    print('The given number is not a Prime Number')
