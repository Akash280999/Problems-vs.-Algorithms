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

    input_list.sort(reverse=True)

    # for adding digits at odd indices
    totalx = 0
    for i in range (0, len(input_list), 2):
        totalx = totalx * 10 + input_list[i]

    # for adding digits at even indices
    totaly = 0
    for i in range (1, len(input_list), 2):
        totaly = totaly * 10 + input_list[i]

    return [totalx,totaly]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)    # output Pass

test_case = [[], []]
test_function(test_case)    # output Pass