def int_from_list(input_list):
    str_list = [str(e) for e in input_list]
    string = "".join(str_list)
    return int(string)


def rearrange_digits_sort(input_list):
    """
    Sort the array first so we can grab alternating values to build our two
    numbers.

    This sort is O(nlog(n)) because for each value in the list, we are
    dividing list in half at most log2(n) times. Adding a new value adds at
    most log2(n) time.

    Args:
            input_list(list): Input list
    Returns:
            (int),(int): Two maximal sums
    """

    # cardinality one => do nothing
    if len(input_list) > 1:

        # midpoint of the input list
        mid_idx = int(len(input_list)/2)

        # upper list and lower list
        ul = input_list[:mid_idx]
        ll = input_list[mid_idx:]

        # recursive call to rearrange the upper and lower halves of the list
        rearrange_digits_sort(ul)
        rearrange_digits_sort(ll)

        # initialize our iteration indices and temp variable for length
        i = j = k = 0
        l = len(input_list) - 1

        # write the upper and lower lists to the input list
        while i < len(ul) and j < len(ll):
            if ul[len(ul) - 1 - i] < ll[len(ll) - 1 - j]:
                input_list[l-k] = ul[len(ul) - 1 - i]
                i += 1
            else:
                input_list[l-k] = ll[len(ll) - 1 - j]
                j += 1
            k += 1

        # take care of any remaining elements
        while i < len(ul):
            input_list[l-k] = ul[len(ul) - 1 - i]
            i += 1
            k += 1

        while j < len(ll):
            input_list[l-k] = ll[len(ll) - 1 - j]
            j += 1
            k += 1


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximal. We alternate largest values remaining from a sorted list. If the
    list that gets the index 0 value from the main list has more digits (at
    most by one) then it will always produce the maximal sum.

    This solution is O(nlog(n)) because for each value in the list, we are
    dividing list in half at most log2(n) times. Adding a new value adds at
    most log2(n) time.

    Args:
            input_list(list): Input list
    Returns:
            (int),(int): Two maximal sums
    """
    # lists of length one  or zero don't produce two values
    if len(input_list) < 2:
        return [-1]

    rearrange_digits_sort(input_list)

    # now make two alternating arrays (this is O(n))
    val_0_list = []
    val_1_list = []

    for i, e in enumerate(input_list):
        if i % 2:
            val_1_list.append(e)
        else:
            val_0_list.append(e)

    # turn those lists into integers
    val_0 = int_from_list(val_0_list)
    val_1 = int_from_list(val_1_list)

    return [val_0, val_1]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# a few more for fun

test_function([[4, 6, 2, 5, 9, 8, 9, 1, 4, 2, 7], [986421, 97542]])
test_function([[0], [-1]])
test_function([[], [-1]])
