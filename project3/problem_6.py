import random
import sys


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Time complexity O(n) (exactly, since we do it all in one pass).

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)
    
    # initialize the maxs/min values to their extremes
    max = -sys.maxsize
    min = sys.maxsize

    # one traversal to rule them all
    for i, e in enumerate(ints):

        # if we have something that isn't an `int`, return `None`s
        if not isinstance(e, int):
            return (None, None)

        # otherwise check and set max/min
        if e > max:
            max = e
        if e < min:
            min = e

    return (min, max)


# Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# a few more for fun
# deck of cards
l = [i for i in range(1, 53)]  # a list containing 1 - 52
random.shuffle(l)
print("Pass" if ((1, 52) == get_min_max(l)) else "Fail")

# a list containing -100000 to 99999 (still quite fast, the shuffle is the slow part)
l = [i for i in range(-100000, 100000)]
random.shuffle(l)
print("Pass" if ((-100000, 99999) == get_min_max(l)) else "Fail")

# a sparse list containing system max and min
l = [-sys.maxsize, -1, 0, 1, sys.maxsize]
random.shuffle(l)
print("Pass" if ((-sys.maxsize, sys.maxsize) == get_min_max(l)) else "Fail")

# a list containing a string
l = ["frank", 0]
print("Pass" if ((None, None) == get_min_max(l)) else "Fail")

# a list containing an empty list
l = [2, []]
print("Pass" if ((None, None) == get_min_max(l)) else "Fail")
