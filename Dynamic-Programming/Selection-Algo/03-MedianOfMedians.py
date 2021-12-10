

def median_algorithm(nums, k):
    
    # we have to split the list into chunks of 5 items
    chunks = [nums[i:i+5] for i in range(0, len(nums), 5)]
    
    # median is the middle item in the sorted order
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
    pivot_val = sorted(medians)[len(medians) // 2]
    
    # Partition Phase
    left_array = [n for n in nums if n < pivot_val]
    right_array = [m for m in nums if m > pivot_val]
    
    # Selection Phase
    pivot_idx = len(left_array)
    if k < pivot_idx:
        # we consider the left_array because we are looking for smaller items
        return median_algorithm(left_array, k)
    elif k > pivot_idx:
        # we consider the right array BUT we hupdate the k value cuz we have created a new array
        return median_algorithm(right_array, k-len(left_array) - 1)
    else:
        return pivot_val
    
def select(nums, k):
    return median_algorithm(nums, k-1)

x = [1,-5, 0, 10, 15, 20, 3, -1, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(select(x, 1))
print(select(x, 2))
print(select(x, 3))
print(select(x, 4))

    