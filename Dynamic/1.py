from functools import wraps                     # For setting function attributes 
from functools import update_wrapper            # For setting class attributes
from functools import lru_cache                 # For caching values
from time import perf_counter as pc             # For calculating time taken

class counter:                                  # Define a decorator class
    def __init__(self, f):                      # Define a constructor
        update_wrapper(self, f)                 # Replace counter's attributes with f's               
        self.f = f
        self.c = 0

    def __call__(self, *args, **kwargs):        # Define a call function
        self.c += 1                             # Increment count
        return self.f(*args, **kwargs)          # Return function call
    
    def max_count(self):                        
        return f'Count: {self.c}'               # Return count 

def timer(f):                                   # Define a decorator function
    @wraps(f)                                   # Replace wrapper's attributes with f's 
    def wrapper(*args, **kwargs):               # Define a wrapper function
        s,a,e = pc(),f(*args,**kwargs),pc()     # s = start time, a = answer, e = end time
        if(str(args[0])=='30'):                 # The query number
            print(f'Time: {(e-s):.8f}s')        # Print compute time
        return a                                # Return answer                              
    return wrapper                              # Return wrapper function

@counter                                        # Counter class Decorator
@timer                                          # Timer function Decorator
def fib1(n):                                    # Define a function
    if n < 2: return n                              
    else: return fib1(n-1) + fib1(n-2)          # Recursive call

@counter                                        # Counter class Decorator 
@lru_cache(maxsize=None)                        # LRU Cache enabled
@timer                                          # Timer function Decorator
def fib2(n):                                    # Define a function
    if n < 2: return n                              
    else: return fib2(n-1) + fib2(n-2)          # Recursive call

@counter                                        # Counter class Decorator 
@timer                                          # Timer function Decorator
def fib3(n, c=None):                            # Define a function
    if n == 0: return 0                         
    if n == 1: return 1

    if c is None: c = {}                        # Initialize cache
    if n in c: return c[n]                      # If value in cache return value

    ans = fib3(n-1, c) + fib3(n-2, c)           # Recursive call
    c[n] = ans                                  # Add value to cache
    return ans                                  # Return value

@counter                                        # Counter class Decorator 
@timer                                          # Timer function Decorator
def fib4(n):                                    # Define a function                    
    a, b = 0, 1                                 # Initialize values
    for z in range(2, n+1): a, b = b, a + b     # Iterative call
    return b                                    # Return value

print("\nWithout Cache: ")
print(f'Output: {fib1(30)}')                    # Call fib1
print(fib1.max_count())                         # Maximum Count

print("\nWith Cache: ")
print(f'Output: {fib2(30)}')                    # Call fib2
print(fib2.max_count())                         # Maximum Count

print("\nTop-Down: ")
print(f'Output: {fib3(30)}')                    # Call fib3
print(fib3.max_count())                         # Maximum Count

print("\nBottom-Up: ")
print(f'Output: {fib4(30)}')                    # Call fib4
print(fib4.max_count())                         # Maximum Count