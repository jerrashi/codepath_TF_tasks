
"""
Problem 1:
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in 
an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

- Understand
1) What do we return if given an empty array?
2) Can there be less/more rabbits in the forest than in the array?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Dynamic - likely
Graphs - unlikely
Stack - unlikely

P - Plan
Write out in plain English what you want to do:
This problem is heavily logic based. If we count the number of rabbits for each response (i.e. we record that there are 2 rabbits that 
responded that there are 3 OTHER rabbits of the same color as them) we can then calculate the minimum number of rabbits using a simple formula.
Given x responses of y rabbits, we know there has to be at least x/(y+1) groups (rounded up). I.e. for our example of 2 rabbits responding 3, we 
know that there are at least 2 / 3+1 groups, which rounds up to 1 group of rabbits composed of 4 rabbits. Math import functions don't always work in 
leetcode, so instead of using math.ceil, the equivalent operation is (x + d - 1)//d where d is the divisor. Thus, we get (x + y)//(y+1).

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        freq = {}

        for i in answers:
            freq[i] = freq.get(i, 0) + 1

        total_sum = 0

        for n, count in freq.items():
            # number of groups = count / n+1 rounded up
            groups = (count + n) // (n + 1)
            # total_sum = groups * (n + 1)
            total_sum += groups * (n + 1)
        
        return total_sum
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time & space complexity

Strength(s):
- linear space and time complexity

Weakness(es):
- can be written in less lines using a counter implementation
"""
"""
Problem 2:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

U - Understand
1) What do we return if given an empty array
2) Are all values non-negative?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Greedy - likely
DFS - unlikely
Union Find - unlikely

P - Plan
Write out in plain English what you want to do:
Basically, we can solve this problem using a custom sort operation. We will sort two numbers x and y by the following operation: if x+y (concatenated)
is greater than y+x (concatenated) then x will come before y. Otherwise, y will come before x. This is a greedy approach since we optimize at a local
level and then keep going until the whole input is optimized.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    from functools import cmp_to_key

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert the list of integers to a list of strings
        nums = list(map(str, nums))
        
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        # Sort the numbers based on the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers into a single string
        largest_num = ''.join(nums)
        
        # Edge case: if the result is all zeros, return "0"
        return '0' if largest_num[0] == '0' else largest_num
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n*klogn) time complexity where n is the number of numbers and k is the length of concatenated strings
O(n*k) space complexity

Strength(s):
- uses greedy approach

Weakness(es):
- have to implement custom compare operation
"""
