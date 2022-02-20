# Problem 3 - Explanation

The list has to be sorted for this, whether that means you sort it before forming your numbers, or you build the values while sorting. The sort again uses repeated bisection to locate the maximal value in the list, recursively sorting it. Then integers of maximal sum, such that they are no more than one digit different in length, are created by taking the even and odd sums of the sorted list. Lists are used to take advantage of the simple splitting functionality.

The sort uses repeated bisection for each element in the list, so it has time complexity of `O(nlog(n))` - _i.e._, it takes at most `log2(n)` bisections for each of the `n` elements in the list. Since it is depth first, we only grow along one branch of the tree, so it has space complexity of `O(n)` (well, `O(3n) = O(n)`).
