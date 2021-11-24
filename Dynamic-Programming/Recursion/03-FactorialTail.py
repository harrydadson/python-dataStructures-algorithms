
def factorial_tail(n, accumulator=1):
    
    # Base Case
    if n == 1:
        return accumulator
    
    # ops
    return factorial_tail(n - 1, n * accumulator)

print(factorial_tail(4))