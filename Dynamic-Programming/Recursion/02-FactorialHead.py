
def factorial_head(n):
    
    # Base Case
    if n == 0:
        return 1
    
    # use recursion
    result1 = factorial_head(n - 1)
    
    # we do some ops
    result2 = n * result1
    return result2

print(factorial_head(4))
    