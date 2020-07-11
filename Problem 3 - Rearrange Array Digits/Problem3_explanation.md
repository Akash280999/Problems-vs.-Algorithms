# Problems vs Algorithms - Problem 3 - Rearrange Array Digits - Explanation

## Logic implemented
Implemented the logic of mergesort. It is a Divide and Conquer algorithm. <br>
So, I used the ```mergesort()``` function which divides input array in two halves recursively till it becomes single unit and then merges the two halves using ```merge()``` and sorts them.

## Run time complexity: ```O(nlog(n))```
Time complexity of Merge Sort is ```O(nlog(n))``` in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.

## Space complexity: ```O(N)```
I used a buffer array of the length equal to the number of inputs , so the space complexity is ```O(n)```