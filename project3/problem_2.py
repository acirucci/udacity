def my_print(string):
    return print(string)

def rotated_array_recursive_search(input_list, li, ui, number):
    if li > ui:
        return -1

    mid_idx = int((ui + li) / 2)

    # match at an endpoint
    if number == input_list[li]:
        return li
    if number == input_list[ui]:
        return ui
    if number == input_list[mid_idx]:
            return mid_idx

    # number is in first half or second half
    if number > input_list[li]:
        # number < middle value => number is in first half of list
        # number > middle value && middle value < first value
        #   => max is in first half of list, so is number
        mid_cmp0 = number < input_list[mid_idx]
        mid_cmp1 = number > input_list[mid_idx] and input_list[mid_idx] < input_list[li]
        if (mid_cmp0) or (mid_cmp1):
            return rotated_array_recursive_search(input_list, li, mid_idx - 1, number)
    
    # if we get here then we are in the second half of list
    return rotated_array_recursive_search(input_list, mid_idx + 1, ui, number)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array.
    Again obvious O(log(n)) since we divide the space in half every time
    and we can't do this more than log2(n) times.

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    return rotated_array_recursive_search(input_list, 0, len(input_list) - 1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    lin_idx = linear_search(input_list, number)
    rot_idx = rotated_array_search(input_list, number)
    if lin_idx == rot_idx:
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# a few more for fun
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 10])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 6])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 7])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 8])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 1])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 2])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 3])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 4])
test_function([[6, 7, 8, 1, 2, 3, 4, 5], 5])
