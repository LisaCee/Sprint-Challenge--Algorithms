#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) space: O(1)
time: O(n) --each program runs n times, regardless of the size of n

b) space: O(1)
time: O(n ^2) --nested loops cause program to increase size based on n

c) time: O(n) -- for each bigger n, the programs must be called n times

## Exercise II

I would tackle this problem as if it were a binary search. I would take all of the floors and divide them by 2. If the egg breaks at height / 2, then I would halve the lower height and repeat until the egg no longer breaks. This would be log time - O(log n)
