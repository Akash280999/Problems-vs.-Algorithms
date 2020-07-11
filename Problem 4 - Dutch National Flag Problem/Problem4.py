def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    one_idx = 0
    zero_idx = 0
    two_idx = len(input_list) - 1

    while one_idx <= two_idx:
        if input_list[one_idx] == 2:
            input_list[one_idx], input_list[two_idx] = input_list[two_idx], input_list[one_idx]
            two_idx -= 1
            continue

        if input_list[one_idx] == 0:
            input_list[one_idx], input_list[zero_idx] = input_list[zero_idx], input_list[one_idx]
            zero_idx += 1

        one_idx += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])    # output Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])   # output Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])    # output Pass
test_function([])   # output Pass
test_function([0])  # output Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])   # output Pass