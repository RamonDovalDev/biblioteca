# Define a class that contains at least two methods: "get_string" to retrieve a string from console input and "print_string" to display the string in uppercase
# Additionally, include a simple test function to validate the class methods.
# Input: str_obj = InputOutString(), str_obj.get_string(), str_obj.print_string()
# Expected Output: If the input string is "hello world", the output will be: "HELLO, WORLD"

class InputOutString:
    def __init__(self):
        self.string = ""
    
    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())

# Test function to validate the class methods
str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()