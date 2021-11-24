

def linear_Search_recursive(container, item, index=0):
    
    # Base Case
    if index >= len(container):
        return -1
    
    # Base Case when we find item
    if container[index] == item:
        return index
    
    return linear_Search_recursive(container, item, index + 1)

nums = [1, 4, 6, -4, 0, 100]
print(linear_Search_recursive(nums, 0))
    