# Problem 4 - Explanation

There might be a more straightforward way to do this, but I decided to simply remove the zeroes and push them on the front of the list, and remove the twos and put them in their own list. I then concatenate the two lists at the end. The rationale is that if you simply try to pop the twos and push them on the end of the list, you will eventually have all twos at the end of the list and you can't know to stop the recursion unless you keep track of the recursion depth.

The time complexity is `O(n^2)` because we traverse the entire list once but the complexity of list concatination is n^2. The space complexity is also `O(n)` because each recursion has its own lexical scope, _i.e._, its own set of local variables.
