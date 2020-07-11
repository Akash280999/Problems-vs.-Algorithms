def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return []

    input_list = mergesort(input_list)

    # for adding digits at odd indices
    totalx = 0
    for i in range(len(input_list) - 1, -1, -2):
        if input_list[i] >= 0:          # to remove negative numbers
            totalx = totalx * 10 + input_list[i]

    # for adding digits at even indices
    totaly = 0
    for i in range(len(input_list) - 2, -1, -2):
        if input_list[i] >= 0:          # to remove negative numbers
            totaly = totaly * 10 + input_list[i]

    return [totalx, totaly]


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_position = 0
    rigth_position = 0

    while left_position < len(left) and rigth_position < len(right):
        if left[left_position] > right[rigth_position]:
            merged.append(right[rigth_position])
            rigth_position += 1

        else:
            merged.append(left[left_position])
            left_position += 1

    merged += left[left_position:]
    merged += right[rigth_position:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print()
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])     # output Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  # output Pass
test_function([[], []])  # output Pass
test_function([[4, 4, 4, 4, 4, 4], [444, 444]])  # output Pass
test_function([[], [0, 0]])  # output Pass
test_function([[9], [9, 0]])    # output Pass
test_function([[1, 2, 3, 4, -1], [42, 31]])     # output Pass