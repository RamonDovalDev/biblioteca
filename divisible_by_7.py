# Write a Python program that identifies all numbers between 7 and 7000 that are divisible by 7 but not a multiple of 5. The numbers should be printed in a comma-separated sequence on a single line.

def find_numbers(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))
    return ','.join(result)

print(find_numbers(7, 7000))