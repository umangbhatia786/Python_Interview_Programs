# Prompt the user to input the length of the array
length = int(input('Enter length of array you wish to create: '))

input_arr = list()

# Populate the array with user input values
for i in range(0, length):
    val = int(input(f'Enter value for index {i}: '))
    input_arr.append(val)

print(f'Array before swapping: {input_arr}')

# Swap the first and last elements of the array
input_arr[0], input_arr[len(input_arr)-1] = input_arr[len(input_arr)-1], input_arr[0]

print(f'Array after swapping: {input_arr}')
