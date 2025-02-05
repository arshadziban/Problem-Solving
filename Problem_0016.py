def test_diff(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False  # Added return statement

# Correct way to call the function
print(test_diff([1, 6, 7, 10]))  # Should print True
print(test_diff([1, 6, 7, 10, 6]))  # Should print False
