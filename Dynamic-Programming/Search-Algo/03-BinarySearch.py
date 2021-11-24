
def binary_search(container, item, left_idx, right_idx):
    
    # Base Case - search missed
    if right_idx < left_idx:
        return -1
    
    # generate idx of middle item
    mid_idx = (left_idx + right_idx) // 2
    
    # found the item
    if container[mid_idx] == item:
        return mid_idx
    
    # check middle item is smaller or greater than item left sub-array
    elif container[mid_idx] > item:
        print("checking items on the left...")
        # discard right sub-array (items greater than the middle item)
        return binary_search(container, item, left_idx, mid_idx - 1)
    
    # item is in the right sub-array    
    elif container[mid_idx] < item:
        print("checking items on the right...")
        return binary_search(container, item, mid_idx + 1, right_idx)
        
nums = [-5, -4, 0, 2, 4, 6, 8]
print(binary_search(nums, 6, 0, len(nums) - 1))
        