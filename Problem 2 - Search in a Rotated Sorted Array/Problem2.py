def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)

    # if no list found
    if type(input_list) != list:
        return -1

    # if empty array found
    if n == 0:
        return -1

    start = 0
    end = n - 1

    while end > start + 1:
        mid = (end + start) // 2

        value = input_list[mid]

        if value == number:
            return mid

        if input_list[start] < value < input_list[end]:
            if number > value:
                start = mid
            else:
                end = mid

        elif value > input_list[start] and value > input_list[end]:
            if input_list[start] <= number < value:
                end = mid
            else:
                start = mid

        elif value < input_list[start] and value < input_list[end]:
            if value < number <= input_list[end]:
                start = mid
            else:
                end = mid

    if input_list[start] == number:
        return start
    elif input_list[end] == number:
        return end
    else:
        return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # print Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # print Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # print Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # print Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # print Pass
test_function([[], 5])  # print Pass