def intersect(nums1, nums2):
    counts = {}
    result = []
    
    for num in nums1:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    
    return result

# Example usage:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2)) 
