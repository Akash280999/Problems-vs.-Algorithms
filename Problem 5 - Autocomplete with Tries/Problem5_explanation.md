# Problems vs Algorithms - Problem 5 - Autocomplete with Tries - Explanation

## Logic implemented
TrieNode and Trie classes were implemented.
* A Trie class that contains the root node (empty string). 
* A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

## Run time complexity: ```O(n)```
Worst case run time complexity is of ```O(n)```, where n is the no. of characters in the word.

## Space complexity: 

The space complexity is of ```O(word_length * unique_chars * no_of_words)```
