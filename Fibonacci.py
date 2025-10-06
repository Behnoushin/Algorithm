# Fibonacci
# - Given an integer n, return the nth Fibonacci number.
# - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
# - Can be solved recursively or iteratively.

def fibonacci(n):
    if n == 0:      
        return 0      
    elif n == 1:     
        return 1       
    else:            
        return fibonacci(n-1) + fibonacci(n-2) 
