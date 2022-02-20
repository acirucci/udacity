# Problem 5 - Explanation

Dictionaries were the obvious choice here because they allow you to return all the keys (and all the key/value pairs) easily. We can then iterate over them.

The `insert` and `find` methods are `O(n)` since they work over the characters in the string. The space complexity of a Trie is (I think?) `O(n)` because you would add a new node for each new character in the worst case scenario.
