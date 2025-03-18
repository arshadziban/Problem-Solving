# Longest Consecutive Sequence
def longest_consecutive(nums):
    num_set = set(nums)  
    max_length = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Example test cases
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [9, 1, 4, 7, 3, 2, 6, 5, 8]

print(longest_consecutive(nums1))  
print(longest_consecutive(nums2))  
