# Q5
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    multiplier = n-k+1
    result = n 
    if k==0:
        return 1
    else:
        while multiplier<n:
            result *= multiplier
            multiplier +=1
        return result 

def falling_alt(n,k):
    sum = 1
    while (k > 0):
        k = k - 1
        sum *= n
        n = n - 1
    return sum

def falling_alt2(n,k):
    total, stop = 1, n-k
    while n > stop:
        total, n = total*n, n-1
    return total

# Q6
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in range(len(str(y))):
        sum += int(str(y)[i])
    return sum

# Alternative:
def sum_digits_alt(y):
    while (x//10):
        sum += x%10
        x = x//10
    sum = sum + x
    return sum

def sum_digits_alt2(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total


def double_eights(n):
    """Return true if n has two adjacent eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    flag = False
    for i in range(len(str(n))-1):
        if int(str(n)[i]) == 8:
            if int(str(n)[i+1]) == 8:
                flag = True
    return flag

def double_eights_alt(n):
    isTure = False
    prev = -1
    while (n):
        temp = n % 10
        if (prev == temp and temp == 8):
            isTure = True
            break
        prev = temp
        n = n // 10
    return isTure


def double_eights_alt2(n):
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False