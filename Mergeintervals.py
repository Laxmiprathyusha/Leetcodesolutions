def mergeintervals(intervals):

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start value
    left = intervals[0]
    merged = []

    for right in intervals[1:]:
        if left[1] >= right[0]:  
            left[1] = max(left[1], right[1]) 
        else:
            merged.append(left)
            left = right
    merged.append(left)  

    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeintervals(intervals))
