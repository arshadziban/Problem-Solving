# Write a Python function that takes a list of integers and returns the second largest number.If the list has less than 2 unique elements, return None.

def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

# Test cases
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(second_largest([3, 3, 3]))            # Output: None
print(second_largest([1]))                 # Output: None
print(second_largest([5, 5, 5, 5, 5]))      # Output: None