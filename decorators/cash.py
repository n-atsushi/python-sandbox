def memoize(func):
    cash = {}
    def _wrapper(n):
        # STEP3
        if n not in cash:
            cash[n] = func(n)
        # STEP6
        return cash[n]
    return _wrapper 

@memoize
def long_func(num: int) -> int:
    # STEP5
    r = 0
    for i in range(1):
        r += num * i
    return r

# STEP 1
for i in range(10):
    # STEP 2
    print(long_func(i))
    
for i in range(10):
    print(long_func(i))
