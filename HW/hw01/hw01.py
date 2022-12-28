# hw link: https://inst.eecs.berkeley.edu/~cs61a/fa20/hw/hw01/
# Solution link: https://cs61a.org/hw/sol-hw01/
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a,b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return x**2+y**2+z**2 - max(x,y,z)**2
    # Alternate solution
    # return min(i*i+j*j, i*i+k*k, j*j+k*k)


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    l = []
    for i in range(1,n):
        if n % i ==0:
            l.append(i)
    return max(l)

# Alternative:
def largest_factor_alt(n):
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1
    # Iterating from n-1 to 1, we return the first integer that evenly divides n. This is guaranteed to be the largest factor of n.
# ****** function's always end when ever there control flow meets a return statement.

def largest_factor_alt2(n):
    factor = n - 1
    while n % factor != 0:
        factor -= 1
    return factor

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return False

def true_func():
    "*** YOUR CODE HERE ***"
    print('42')

def false_func():
    "*** YOUR CODE HERE ***"
    print('47')

# Call to check: 
# python3 ok -q with_if_statement
# python3 ok -q with_if_function

# 从逻辑上讲，with_if_statement和with_if_function是相同的。但是，从解释器的角度来看这两个函数，它们是不同的。
# with_if_function函数使用一个调用表达式，它保证它的所有操作数子表达式在if_function应用于结果参数之前都会被计算。因此，即使c返回False，该函数t也会被调用。相比之下，如果返回 False，with_if_statement则永远不会调用。
# So far I've come to understand that the if statement in the with_if_statement checks to see if c() is T/F, and then executes accordingly. Whereas the if_function executes everything at once, 
# so cond(), true_func(), and false_func() are all run through and that way you get the ZeroDivisionError with the with_if_function. The with_if_statement, 
# on the other hand, won't touch the t() if c() is false because python will just move on to the else: and to the f() respectively.

###** Remeber that when we call a function, we must evaluate every operand as parameter in the function, 
###** so anyway, cond function, true_func function and false_func function must be called regardless of the return value(True or False) by cond function, 
### while in if statement, the true clause can not be called if evaluated value is False. So the two is not exactly the same.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    m=1
    print(n)
    while n>1:
        if n % 2 == 0:
            n = n//2  # Integer division prevents "1.0" output
            print(n)
            m += 1
        else: 
            n = n * 3 + 1
            print(int(n))
            m += 1
    return m
        
    

