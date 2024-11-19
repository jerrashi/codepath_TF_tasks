"""
Problem 1:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

- Understand
1) Do we need to return the series or just the length?
2) Are we allowed to create new data structures?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Sets - likely
DFS - unlikely
Backtracking - likely

P - Plan
Write out in plain English what you want to do:
Given that it takes O(n) time to put items in a set and set item retrieval is O(n) time, the most efficient way to solve this problem in O(n) time 
is to put all the items in a set and iterate through the items. We run a second loop if the number before the number (i.e. 2 when looking at 3) is
not in the set since it may be the start of a new / longer sequence. Then, we iterate through consecutive numbers and check if they are in the set.
If so, we increase the current_sequence variable. Once the sequence is broken, we set the return variable longest_sequence to whichever is longer:
current_sequence or longest_sequence.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the length of the consecutive sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity since each number is checked at most once (we only start the loop if the number is the start of a sequence, meaning n-1 is not
in the set)
O(n) space complexity since we make a set of the given numbers

Strength(s):
- O(n) time and space complexity

Weakness(es):
- uses a set, which may not be allowed by the interviewer
"""

"""
Problem 2:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then
immediately sell it on the same day.

Find and return the maximum profit you can achieve.

U - Understand
1) If we buy and sell a stock on the same day do we make zero profit?
2) Are all stock values non-negative?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
BFS - unlikely
DFS - unlikely
Backtracking - unlikely

P - Plan
Write out in plain English what you want to do:
If we draw out this problem, we realize it's pretty simple - we buy and sell anytime we can make a profit, or in other words, any time prices[n] >
prices[n-1]. In those cases, we conduct that trade (buying then selling) and make prices[n]-prices[n-1] in profit. If only real life stock broking
was this easy. :')

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]

        return profit
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity
O(1) space complexity

Strength(s):
- O(n) time complexity and O(1) space complexity

Weakness(es):
- doesn't tell you what actual trades to make, so in a more difficult/expanded version of this problem this solution wouldn't work
"""
