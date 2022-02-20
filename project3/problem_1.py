# Get the midpoint of two values (ceil of midpoint if distance is odd)
def midpoint(lv, hv):
    if lv > hv:
        return 0

    v = hv + lv

    # if difference is even, return the midpoint, otherwise the ceil of midpt
    if v % 2 == 0:
        #print("Midpoint is {}/2 = {}".format(v, int(v/2)))
        return int(v/2)
    else:
        #print("Midpoint is {}/2 = {}".format(v, int((v + 1) / 2)))
        return int((v + 1) / 2)

# Recursively find the root
def get_root(n, lb, ub):
    mp = midpoint(lb, ub)
    test = mp * mp

    # no consecutive square is more than 2mp+1 away: (mp + 1)^2 - mp^2 = 2mp + 1
    if (n >= test) and ((n - test) < 2 * mp + 1):
        #print("Returning {}".format(mp))
        return mp

    # otherwise, recursive search by halves
    if test < n:
        #print("{} is less than {}, so ({}, {})".format(test, n, mp, ub))
        return get_root(n, mp, ub)
    else:
        #print("{} is more than {}, so ({}, {})".format(test, n, lb, mp))
        return get_root(n, lb, mp)

def sqrt(number):
    """
    Calculate the floored square root of a number.
    Obviously this is O(log(n)) since you can't divide an integer in half into
    an integer more than log2(n) times - that's the definition of log2..

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    # Need an integer
    if not isinstance(number, int):
        return -2
    # Need a nonnegative integer
    if number < 0:
        return -1

    # the first few cases are easy
    if number < 1:
        return 0
    if number < 4:
        return 1
    if number < 9:
        return 2

    # for all integers j > 4, sqrt(j) < j / 2, so we can just test those values
    upper_bound = midpoint(0, number)
    lower_bound = 0
    return get_root(number, lower_bound, upper_bound)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# A few more for fun
print ("Pass" if  (-1 == sqrt(-3)) else "Fail")
print ("Pass" if  (-2 == sqrt("frank")) else "Fail")
print ("Pass" if  (16 == sqrt(257)) else "Fail")
print ("Pass" if  (43 == sqrt(1935)) else "Fail")

