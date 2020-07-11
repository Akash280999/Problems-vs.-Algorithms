# Problems vs Algorithms - Problem 7 - Request Routing in a Web Server with a Trie - Explanation

## Logic implemented
RouteTrieNode, RouteTrie and Router classes were implemented.
I have implemented an HTTPRouter like we would find in a typical web server using the Trie data structure.
A Trie with a single path entry of: ```/about/me``` would look like:

```(root, None) -> ("about", None) -> ("me", "About Me handler")```
## Run time complexity: ```O(n)```
The run time complexity of insert and search is of ```O(n)```, where n is the number of tokens upon splitting the path with "/" character.

## Space complexity
The space complexity is of ```O(token_length * unique_tokens * no_of_tokens)```
