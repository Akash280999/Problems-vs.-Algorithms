# Problems vs Algorithms - Problem 3 - Rearrange Array Digits - Explanation

## Logic implemented
Python uses an algorithm called Timsort. Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort. <br>
Here I have used sort(), built-in function.

## Run time complexity: O(nlog(n))
The built in sort() function has time complexity of ```O(nlog(n))```.

## Space complexity: O(1)
The sort method sorts a list in place, it does use some additional space, as stated in the [description](https://github.com/python/cpython/blob/master/Objects/listsort.txt) of the implementation. 
Therefore the worst case space complexity is ```O(N)``` and best case ```O(1)```