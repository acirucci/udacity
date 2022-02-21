# Problem 7 - Explanation

Dictionaries were the obvious choice here because they allow you to return all the keys (and all the key/value pairs) easily. We can then iterate over them. Adding a not found handler is as easy as returning the handler when the route is not found, in this case when the `find` method from `RouteTrie` returns a `None`. Handling trailing slashes is accomplished by checking the `-1` index in the path string.

The `insert` method has time complexity `O(n)` and space complexity of `O(n)`

The `split_path` method has time complexity `O(n) and space complexity of `O(n)`

The `find` method has time complexity `O(n)` and space complexity of `O(n)`

Tries have `O(n)` time complexity and `O(1)` space complexity
