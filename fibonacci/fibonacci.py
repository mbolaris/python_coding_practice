'''
Created on Jan 30, 2017
@author: mbolaris
A variety of methods for computing the nth fibonacci number
'''

def naive(n):
    '''
    A naive recursive method to compute the nth fibonacci number
    Returns:
        int: The nth fibonacci number
    '''
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return naive(n - 1) + naive(n - 2)

def memoized(n, _cache=None):
    '''
    A memoized recursive method to compute the nth fibonacci number
    Returns:
        int: The nth fibonacci number
    '''
    if _cache is None:
        _cache = {}

    if n in _cache:
        return _cache[n]

    if n < 1:
        _cache[n] = 0
    elif n == 1:
        _cache[n] = 1
    else:
        _cache[n] = memoized(n - 1, _cache) + memoized(n - 2, _cache)
    return _cache[n]

def tabulation(n):
    '''
    A method to compute the nth fibonacci number using tabulation
    Returns:
        int: The nth fibonacci number
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        first_fib = 0
        second_fib = 1
        for _ in range(2, n + 1):
            next_fib = first_fib + second_fib
            first_fib = second_fib
            second_fib = next_fib

    return second_fib
