# Problem 1 - Explanation

The solution relies on repeated bisection of the interval, excluding the half that doesn't contain the target value, checking the endpoints and midpoint, then repeating this process by recursion. Once one resursion finds the correct value, it is returned up the stack. Since we already tested the endpoints, they could be excluded at each iteration to make it marginally faster. I guess it's clear that I used lists since they are easily split using the `l[a:b]` notation.

The time complexity is `O(log(n))` since the interval can only be halved `log2(n)` times (this is a/the definition of `log2(n)`). Each new iteration stores one more midpoint and test variable, so the space complexity is also `O(log(n))`.
