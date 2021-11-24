
def fibonacci_head(n):
    
    # Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # make reursive func call(s)
    fib1 = fibonacci_head(n - 1)
    fib2 = fibonacci_head(n - 2)
    
    # make some ops
    result = fib1 + fib2
    
    return result

print(fibonacci_head(20))