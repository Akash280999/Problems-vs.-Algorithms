def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        int(number)
        if number<0 or type(number)==float:
            return None

        # base case
        # Square root of 0 or 1 is the number itself
        if (number == 0 or number == 1):
            return number

        # Binary Search for finding the floor value of square root
        ans = 0
        start = 1
        end = number
        while (start <= end):
            mid = (start + end) // 2

            # If the number is a perfect square
            if (mid * mid == number):
                return mid
            # when mid*mid is smaller
            if (mid * mid < number):
                start = mid + 1
                ans = mid
            else:
                # If mid*mid is greater
                end = mid - 1
        return ans
    except Exception :
        return None

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt('Hello')) else "Fail")
print ("Pass" if  (None == sqrt(-34)) else "Fail")
print ("Pass" if  (None == sqrt(14.3)) else "Fail")