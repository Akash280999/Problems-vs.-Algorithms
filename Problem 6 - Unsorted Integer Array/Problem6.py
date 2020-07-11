def get_min_max(array):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
       :param array:
    """
    if len(array) <= 1:     # if empty array passed or having only one element
        print([])
        return None

    min_value = array[0]
    max_value = array[len(array) - 1]

    for number in array:
        if array[number] > max_value:
            max_value = array[number]
        else:
            if array[number] < min_value:
                min_value = array[number]

    return min_value, max_value


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9

for i in range(4):
    random.shuffle(l)
    print(l)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")     # should print Pass for 4 test cases as it in loop
    print()

print ("Pass\n" if (None == get_min_max([])) else "Fail")     # should print Pass
print ("Pass\n" if (None == get_min_max([0])) else "Fail")     # should print Pass