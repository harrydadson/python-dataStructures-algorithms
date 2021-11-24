
def fibonacci_tail(n, a=0, b=1):
    
    # Base Case
    if n == 0:
        return a
    if n == 1:
        return b
    
    # make ops
    return fibonacci_tail(n-1, b, a + b)

print(fibonacci_tail(20))

