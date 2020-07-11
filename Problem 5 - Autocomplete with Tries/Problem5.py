#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate they key components of a Trie or Prefix Tree. A trie is a tree like data structure that stores a dynamic set of strings.   Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search. Before we move into the autocomplete function we need to create a working trie for storeing strings.  We will create two classes, a Trie which contains the root node (empty string) and exposes the general functionality of the Trie like inserting a word or finding the node which represents a prefix.   Give it a try by implementing the TrieNode and Trie classes below!

# In[17]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self,end=False):
        ## Initialize this node in the Trie
        self.end = end
        self.character = dict()
    
    def insert(self, char):
        ## Add a child node in this Trie
        child_node = TrieNode()
        self.character[char] = child_node

        return child_node 
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        node = TrieNode()
        self.root = node

    def insert(self, word):
        ## Add a word to the Trie
        currnode = self.root

        for char in word:
            if char in currnode.character:
                currnode = currnode.character[char]
            else:
                newnode = currnode.insert(char)
                currnode = newnode
        currnode.end = True
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        currnode = self.root
        
        for char in prefix:
            if char in currnode.character:
                currnode = currnode.character[char]
            else:
                return None

        return currnode


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.   To do that we need to implement a new function on the TrieNode object that will return all compelte word suffixes that exist below it in the trie.  e.h. if our Trie contains the words: `["fun", "function", "factory"]` and we as for suffixes from the `f` node we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()` 
# 
# Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go)

# In[18]:


class TrieNode:
    def __init__(self, end=False):
        ## Initialize this node in the Trie
        self.end = end
        self.character = dict()
    
    def insert(self, char):
        ## Add a child node in this Trie
        node = TrieNode()
        self.character[char] = node

        return node
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = list()

        def find_suffix(node, output):

            if node.end:
                result.append(output)

            for char in node.character:
                temp = output + char
                find_suffix(node.character[char], temp)

        find_suffix(self, "")

        return result


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[19]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find('f')
print(node.suffixes())

