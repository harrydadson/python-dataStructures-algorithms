
def tail(n):
    
    # Base Case
    if n == 0:
        return
    
    # we do some ops, operation = print()
    print(n)
    
    # make the recursive func call
    tail(n - 1)
    
def head(n):
    
    # Base Case
    if n == 0:
        return
    
    # we make recursive call
    head(n - 1)
    
    # we can do any ops, operation = print()
    print(n)