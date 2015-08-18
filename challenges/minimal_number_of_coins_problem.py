"""
Minimal number of coins problem
"""

def possibilities(value, coins_available, coins_used):
    if sum(coins_used) == value:
        yield coins_used
    elif sum(coins_used) > value:
        pass
    elif coins_available == []:
        pass
    else:
        for c in possibilities(value, coins_available[:], coins_used + [coins_available[0]]):
            yield c
        for c in possibilities(value, coins_available[1:], coins_used):
            yield c

def get_all_possibilities(value, coins):
    solutions = [s for s in possibilities(value, coins, [])]
    return solutions

def get_minimal_number_of_coins(value, coins):
    solutions = get_all_possibilities(value, coins)
    return len(min(solutions, key=len))

coins, value = [25, 10, 5, 1], 31
print 'Coins that could be used: 25, 10, 5, 1'
print 'Value to return 31'
print "All possible combinations:\n"
for solution in get_all_possibilities(value, coins):
    print solution
print "Minimal number of coins used is: {0}".format(
    get_minimal_number_of_coins(value, coins))