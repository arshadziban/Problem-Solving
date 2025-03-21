# roduct of Array Except Self
def product_except_self(nums):
    n = len(nums)
    output = [1] * n

    # Compute prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and multiply with prefix products
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

# Test cases
print(product_except_self([1,2,3,4]))       
print(product_except_self([-1,1,0,-3,3]))   
