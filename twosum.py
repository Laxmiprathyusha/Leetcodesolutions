def two_sum(nums, target):
    num_dict = {}  # Dictionary to store number and its index
    for index, num in enumerate(nums):
        complement = target - num  # The number needed to reach the target
        if complement in num_dict:
            return [num_dict[complement], index]  # Return the indices of the two numbers
        num_dict[num] = index  # Add the number and its index to the dictionary
    return []  # In case no solution is found, though the problem guarantees one

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
