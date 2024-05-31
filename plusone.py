def moveZeroes(nums):
    # Pointer for the position of the next non-zero element
    nonzero_ele_position = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the current element with the element at non_zero_position
            nums[nonzero_ele_position], nums[i] = nums[i], nums[nonzero_ele_position]
            # Move the non_zero_position pointer to the right
            nonzero_ele_position += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  
