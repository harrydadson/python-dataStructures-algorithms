import random

class QuickSelect:
    
    def __init__(self, nums):
        self.nums = nums
        self.first_idx = 0
        self.last_idx = len(nums)-1
        
    def run(self, k):
        return self.select(self.first_idx, self.last_idx, k-1)
    
    # Partition Phase
    def partition(self, first_idx, last_idx):
        
        # generate a random value within the range [first, last]
        pivot_idx = random.randint(first_idx, last_idx)
        
        self.swap(pivot_idx, last_idx)
        
        for i in range(first_idx, last_idx):
            if self.nums[i] < self.nums[last_idx]: #change to greater >: to find largest item
                self.swap(i, first_idx)
                first_idx += 1
        
        self.swap(first_idx, last_idx)
        
        # index of the pivot
        return first_idx
                            
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        
    
    # Selection Phase
    def select(self, first_idx, last_idx, k):
        
        pivot_idx = self.partition(first_idx, last_idx)
        
        # selection phase when we compare the pivot_idx with k
        if pivot_idx < k:
            # we have to discard the left sub-array and keep considering items on right
            return self.select(pivot_idx + 1, last_idx, k)
        elif pivot_idx > k:
            # we have to discard the right sub-array
            return self.select(first_idx, pivot_idx-1, k)
        # we have found the item we are lokking for
        return self.nums[pivot_idx]
    
    
x = [1, 2, -5, 10, 100, -7, 3, 4]
select = QuickSelect(x)
# first smallest item: -7, second: -5
print(select.run(2))
            
            