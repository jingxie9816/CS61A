this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    increment = 0
    def adder(b):
        nonlocal increment
        result = a + b + increment
        increment += 1
        return result
    return adder


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    x = -1
    def fib():
        nonlocal x 
        x += 1
        def helper(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            else:
                return helper(i-1) + helper(i-2)
        return helper(x)
    return fib

# Alternative: Not use recursion, but record the result of each fib value, and add the previous two up when the function called. 
"""
    n = 0
    m = 1
    index = -1
    def fib():
        nonlocal n,m,index
        index += 1
        if index == 0:
            return n
        if index == 1:
            return m

        res = m + n
        n = m
        m = res
        return res
    return fib
"""


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    temp = [i for i in range(len(lst)) if lst[i] == entry]
    increment = 1
    for j in temp:
        lst.insert(j+increment, elem)
        increment += 1
    return lst


# Alternative:
"""
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            lst.insert(index + 1, elem)
            if entry == elem:           # Avoid the situation of infinately inserting.
                index += 1
        index += 1
    return lst
"""

# Alternative solution
"""
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            lst.insert(index + 1, elem)
            index += 2
        else:
            index += 1
    return lst
"""


