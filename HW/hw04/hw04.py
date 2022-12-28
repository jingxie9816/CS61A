def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance -= amount
                return balance
        elif message == 'deposit':
            balance += amount
            return balance
        else:
            return 'Invalid message'
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    error = 0
    error_list = []
    def withdraw(amount, pw):
        nonlocal balance, error, error_list  # Alternative: use len(error_list) as replacement of error, so that only have 2 nonlocal variables. 
        if error >= 3:
            return "Frozen account. Attempts: " + str(error_list)
        else:
            if pw == password:
                if amount > balance:
                    return 'Insufficient funds'
                else:
                    balance -= amount
                    return balance
            else:
                error += 1
                error_list.append(pw)
                return 'Incorrect password'
    return withdraw



def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    count = 1
    if k == 1:
        return next(t)
    else:
        pre = next(t)
        curr = next(t)
        while True:
            if pre == curr:
                count += 1
                if count == k:
                    return curr
            else:
                count = 1
            pre = curr
            curr = next(t)

# Alternative:
"""
    cnt, prev = 1, next(t)     # t is an iterator
    for item in t:             # Since t is an iterator, after the first next(), t only remains the left items, not the first one. 
        if item == prev: 
            cnt += 1
            if cnt == k:
                return item
        else:
            cnt = 1
        prev = item
"""


def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    # Hints:
    # permutations([1,2,3])
    # ==> 1 + permutations([2, 3]) ## gives 1 + {[2,3], [3,2]} -> [1,2,3], [1,3,2]
    # and 2 + permutations([1, 3]) ## gives 2 + {[1,3], [3,1]} -> [2,1,3], [2,3,1]
    # and 3 + permutations([1, 2]) ## gives 3 + {[1,2], [2,1]} -> [3,1,2], [3,2,1]
    if len(seq) == 1:
        yield seq
    else:
        for i in range(len(seq)):
            for sub_seq in permutations([seq[j] for j in range(len(seq)) if j != i]):
                yield [seq[i]] + sub_seq
# Alternative:
"""
    if not seq:
        yield []
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + [seq[0]] + perm[i:]
"""

def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    return_value = withdraw(0, old_pass)
    if type(return_value) == str:
        return return_value
    else:
        def withdraw_func(amount, password):
            if password == new_pass:
                return withdraw(amount, old_pass)
            else:
                return withdraw(amount, password)
    return withdraw_func

# Alternative:
"""
    test = withdraw(0, old_password)
    if type(test) == str:
        return test

    def joint_withdraw(amount, pwd):
        if pwd == old_password or pwd == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, pwd)

    return joint_withdraw
"""

def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def gen(i):
        m = naturals()
        while True:
            n = next(m)
            if n % 4 == i:
                yield n 
    for i in range(m):
        yield gen(i)

# Alternative:
"""
    def gen(i):
        for e in naturals():     # For loop has the same effect as next()
            if e % m == i:
                yield e
    for i in range(m):
        yield gen(i)
"""

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

