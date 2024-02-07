#Python program to swap 2 numbers

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

print(f'Numbers before swapping, num1={num1} and num2={num2}')

num1, num2 = num2, num1

print(f'Numbers after swapping, num1={num1} and num2={num2}')