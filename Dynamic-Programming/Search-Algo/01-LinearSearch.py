
def linear_search(container, item):
    
    # runtime -> O(N)
    
    for index in range(len(container)):
        if container[index] == item:
            return index
    
    # search miss - when the item is not present in the container
    return -1

nums = [1, 5, -3, 10, 55, 100]
print(linear_search(nums, 10))