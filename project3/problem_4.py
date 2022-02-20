def sort_012_internal(input_list, twos_list, i):
    l = len(input_list)
    if i == l:
        return input_list

    # same scope as return (not necessary in python? but seems confusing to read otherwise)
    ones_and_zeros_list = []

    # get element at index i to compare
    e = input_list[i]

    # if it's a 0, remove it and push it on the front of the list, next element at i+1
    if e == 0:
        del input_list[i]
        input_list.insert(0, 0)
        ones_and_zeros_list = sort_012_internal(
            input_list, twos_list, i + 1)

    # if it's a 2, remove it and put it in the 2s list, otherwise if we append it, at the end we hit an infinite loop
    # next element at i since they all rotate left one
    elif e == 2:
        del input_list[i]
        twos_list.append(2)
        ones_and_zeros_list = sort_012_internal(
            input_list[0:len(input_list)], twos_list, i)

    # if it's a 1, leave it and move to the next element at i+1
    else:
        ones_and_zeros_list = sort_012_internal(
            input_list, twos_list, i + 1)

    # the 2s list populates, just return the 1s and 0s
    return ones_and_zeros_list


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # sorted() returns empty list if input is empty
    if len(input_list) < 2:
        return input_list

    # split it into a list for 0s and 1s, and one for 2s
    # This prevents having to worry about infinite loop when only have 2s left
    twos_list = []
    ones_and_zeros_list = sort_012_internal(input_list, twos_list, 0)

    # concatenate them together
    return ones_and_zeros_list + twos_list


def test_function(test_case):
    # make a copy to test since sorted() alters original
    copy = test_case

    python_sorted_array = sorted(test_case)
    my_sorted_array = sort_012(copy)

    if my_sorted_array == python_sorted_array:
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
              2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# and a few more for fun
test_function([])
test_function([0])
test_function([1])
test_function([2])
test_function([2, 1, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2])
