# Create a Python function that takes a sequence of comma-separated numbers as input and generates both a list and a tuple containing those numbers.
# Input: convert_input_to_list_and_tuple("3,6,5,3,2,8")
# Output: ([3, 6, 5, 3, 2, 8], (3, 6, 5, 3, 2, 8))

def convert_input_to_list_and_tuple(input_string):
    values = input_string.split(',')
    return values, tuple(values)
print(convert_input_to_list_and_tuple("3,6,5,3,2,8"))