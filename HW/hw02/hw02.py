HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        if x == 8:
            return 1
        else:
            return 0
    else:
        return num_eights(x // 10) + (x % 10 == 8)
    #or return num_eights(x // 10) + num_eights(x % 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    
    def helper(index, ppn, dir):
        if n == 1:
            return 1
        elif index != n:
            if index % 8 == 0 or num_eights(index) > 0:
                print("DEBUG:", dir) 
                return helper(index+1, ppn-dir, -dir)  # Generate index=9(the next one of key swaps), so add the opposite direction. ppn+(-dir)

            else:
                return helper(index+1, ppn+dir, dir)
        else:
            return ppn 
    return helper(1,1,1)

#Alternative solution:
"""
    def term(count, value, step):
        if count > n:
            return value
        elif count % 8 == 0 or num_eights(count)>0  :
            return term(count + 1, value + step, -step)
        else:
            return term(count + 1, value + step, step)

    return term(1, 0, 1)
"""
#Solution:
"""
    def helper(result, i, step):
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)
"""

# Alternate solution 1
"""
def pingpong_next(x, i, step):
    if i == n:
        return x
    return pingpong_next(x + step, i + 1, next_dir(step, i+1))

def next_dir(step, i):
    if i % 8 == 0 or num_eights(i) > 0:
        return -step
    return step
"""
# Alternate solution 2
"""
def pingpong_alt(n):
    if n <= 8:
        return n
    return direction(n) + pingpong_alt(n-1)

def direction(n):
    if n < 8:
        return 1
    if (n-1) % 8 == 0 or num_eights(n-1) > 0:
        return -1 * direction(n-1)
    return direction(n-1)
"""


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        all_but_last, last = n // 10, n % 10
        all_but_second_last, second_last = all_but_last // 10, all_but_last % 10
        if last == second_last or last == second_last + 1:
            return missing_digits(all_but_last)
        else:
            return missing_digits(all_but_last) + last - second_last - 1

# Alternative:
    # combine consecutive digits situation with the normal one, because 2-1-1 = 0
    # Only leave along the same digits situation because 2-2-1 = -1
"""  
    if n < 10 :
        return 0 
    else:
        all_but_last, last = n // 10, n % 10
        all_but_second_last, second_last = all_but_last // 10, all_but_last % 10
        if last - second_last -1 == -1:
            return missing_digits(all_but_last)
        else:
            return missing_digits(all_but_last) + last - second_last - 1
"""

def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

from ucb import trace


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(total, smallest_coin):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if smallest_coin is None:
            return 0
        with_smallest_coin = helper(total - smallest_coin, smallest_coin)
        without_smallest_coin = helper(total, next_largest_coin(smallest_coin))
        return with_smallest_coin + without_smallest_coin
    return helper(total, 1)


# Alternatives:
def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins_alt(change):
    def constrained_count_small(change, largest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if largest_coin == None:
            return 0
        without_coin = constrained_count_small(change, next_smaller_coin(largest_coin))
        with_coin = constrained_count_small(change - largest_coin, largest_coin)
        return without_coin + with_coin
    return constrained_count_small(change, 25)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """

    return (lambda f: f(f)) (lambda f: lambda n: 1 if n == 1 else mul(n, f(f)(n- 1)))

