# ind the Majority Element
def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums1))  
print(majority_element(nums2))  
