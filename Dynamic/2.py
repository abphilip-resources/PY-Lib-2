import math

def change_making(denominations, target):
    cache = {}

    def subproblem(i, t):
        if (i, t) in cache: return cache[(i, t)]  # memoization
        val = denominations[i]
        if val > t:
            choice_take = math.inf
        elif val == t:
            choice_take = 1
        else:
            choice_take = 1 + subproblem(i, t - val)

        if i == 0:
            choice_leave = math.inf
        else:
            choice_leave = subproblem(i - 1, t)

        optimal = min(choice_take, choice_leave)
        cache[(i, t)] = optimal
        return optimal

    return subproblem(len(denominations) - 1, target)

def flowerbox(nutrient_values):
    a = 0  
    b = 0 
    for val in nutrient_values:
        a, b = b, max(a + val, b)
    return b

print(f'flowerbox([3, 10, 3, 1, 2]) = {flowerbox([3, 10, 3, 1, 2])}')
print(f'flowerbox([9, 10, 9]      ) = {flowerbox([9, 10, 9])}')
print(
    'change_making([1, 5, 12, 19], 16) = '
    f'{change_making([1, 5, 12, 19], 16)}')