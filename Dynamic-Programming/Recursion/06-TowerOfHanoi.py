'''
- consists of 3 rods and number of disks of different sizes which can slide onto any rod
- starts with disks in a neat stack in ascending order of size on one rod, smallest at the top
- # 0f moves = 2^n - 1, O(n), exponential time complexity

   Rules
- only one disk can be moved at a time
- each move consists of taking the upper disk from one of the stacks and placing it on top of another 
    stack -> a disk can only be moved if it is the uppermost disk on a stack
- No disk may be placed on top of a smaller disk
'''

def hanoi(disk, source, middle, dest):

    '''
    starting_rod, source, A
    middle_rod, middle, B
    end_rod, destination, C
    '''
    
    # Base Case, index 0 is always the smallest plate
    # manipulate smallest plate in the base case
    if disk == 0:
        # move disk from source to dest
        print(f"disk {disk}, {source}, {dest}")
        return
    
    hanoi(disk - 1, source, dest, middle)
    print(f"disk {disk}, {source}, {dest}")
    hanoi(disk - 1, middle, source, dest)
    