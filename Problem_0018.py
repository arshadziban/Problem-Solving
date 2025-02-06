# Write a Python program to make combinations of 3 digits.

# Create an empty list
numbers = []

for num in range(1000):
    # Convert the number to a string and fill with zeros to make it three digits long.
    num = str(num).zfill(3)

print(num)

numbers.append(num)