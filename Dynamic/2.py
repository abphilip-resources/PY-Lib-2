import math                                             # Import math module

def change(denominations, target):                      # Declare function for Problem 1
    cache = {}                                          # Initialize cache

    def rec(i, t):                                      # Declare inner function
        if (i, t) in cache: return cache[(i, t)]        # Return if value in cache
        val = denominations[i]                          # Get value of current coin
        if val > t: y = math.inf                        # If value > target, chance = infinity
        elif val == t: y = 1                            # If value == target, chance = 1
        else: y = 1 + rec(i, t-val)                     # Else, chance = 1 + rec(reduced target)

        if i == 0: n = math.inf                         # If at end of coins, chance = infinity
        else: n = rec(i-1, t)                           # Else, chance = rec(new denomination)

        optimal = min(y, n)                             # Optimal is least value of chance
        cache[(i, t)] = optimal                         # Store optimal value in cache
        return optimal                                  # Return optimal value

    return rec(len(denominations)-1, target)            # Call inner function and return output

def flowerbox(val):                                     # Declare function for Problem 2
    a, b = 0, 0                                         # Initialize a and b
    for v in val: a, b = b, max(a+v, b)                 # Iterate to find max value
    return b                                            # Return max value

print("\nDenomination Problem: ")                       # Solution 1
print(f'No. of notes to make $16 using \
[1, 5, 12, 19] = {change([1, 5, 12, 19], 16)}')         # Scenario A     
print(f'No. of notes to make $17 using \
[1, 5, 12, 19] = {change([1, 5, 12, 19], 17)}')         # Scenario B

print("\nFlower Box Problem: ")                         # Solution 2
print(f'Maximum non consecutive height from \
[3, 10, 3, 1, 2] = {flowerbox([3, 10, 3, 1, 2])}')      # Scenario A
print(f'Maximum non consecutive height from \
[9, 10, 9] = {flowerbox([9, 10, 9])}')                  # Scenario B