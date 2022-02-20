'''
Copy this and run it in a Jupyter notebook to get the input box.
'''

from ipywidgets import interact
from IPython.display import display
from ipywidgets import widgets


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = {}
        self.end_of_word = False

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        # initialize the list
        suffixes = []

        # add the current suffix if it's the end of a word
        if self.end_of_word:
            suffixes.append(suffix)

        # now recurse through the children
        for char, child in self.children.items():
            suffixes.extend(child.suffixes(suffix + char))

        return suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        # let's leverage the find method, init the prefix
        prefix = ""
        for c in word:
            prefix += c  # add another letter from the word
            # insert it if it doesn't exist already
            if self.find(prefix) == None:
                current_node.insert(c)
            # update the current node
            current_node = current_node.children[c]
        current_node.end_of_word = True

    def find(self, prefix):
        # Find and return the Trie node that represents this prefix
        current_node = self.root
        for c in prefix:
            # no valid node => return None
            if c not in current_node.children.keys():
                return None
            # update the current node
            current_node = current_node.children[c]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')

'''
Comment in these test cases and comment out the interactive stuff to test it
without Jupyter.
'''
'''
f("a")
f("an")
f("ant")
f("any")  # any not found
f("f")
f("fa")
f("fu")
f("tr")
f("th")  # th not found
'''
