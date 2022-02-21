# Problem 7 - Explanation

Dictionaries were the obvious choice here because they allow you to return all the keys (and all the key/value pairs) easily. We can then iterate over them. Adding a not found handler is as easy as returning the handler when the route is not found, in this case when the `find` method from `RouteTrie` returns a `None`. Handling trailing slashes is accomplished by checking the `-1` index in the path string.

The `insert`, `split_path`, and `find` methods are `O(n)` since they work over the characters in the string. The space complexity of a Trie is (I think?) `O(n)` because you would add a new node for each new character in the worst case scenario.
