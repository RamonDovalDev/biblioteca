# Create a Python function that takes an integer (n) as input and generates a dictionary containing pairs ( (i, i^2) ) for all integers ( i ) from 1 to ( n ) (inclusive). The function should then return this dictionary.

def generate_square_dict(n):
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i
    return d
print (generate_square_dict(10))
