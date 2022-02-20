# Problem 2 - Explanation

The solution relies on repeated bisection of the interval, excluding the half that doesn't contain the target value, checking the endpoints and midpoint, then repeating this process by recursion. Once one resursion finds the correct value, it is returned up the stack. I used lists since they are easily split using the `l[a:b]` notation.

The time complexity is `O(log(n))` since the interval can only be halved `log2(n)` times (this is a/the definition of `log2(n)`). Each new recursion stores one more set of locally scoped variables, so the space complexity is also `O(log(n))`.
