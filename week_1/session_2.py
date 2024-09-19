"""
Problem 1:
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

U - Understand
1) (Edge case) If n is already 1, do we return 0?
2) Do we have any space or time complexity considerations to make?
M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
BFS - likely
Graphs - likely
Linked List - unlikely
P - Plan
Write out in plain English what you want to do:
One approach, using BFS, is to try out each possible operation at each step. As with typical BFS, we create a queue and store the current number and step count of each number in the queue.
If number is even, we simply do floor division by 2. If number is odd, we add number + 1 and number -1 to the queue.
If number is 1, we return the number of steps we have taken. Since BFS explores at each level equally, it is optimal for finding the shortest distance between nodes in a graph and is optimal here
to find the shortest number of steps to 1.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
from collections import deque

class Solution(object):
    def integerReplacement(self, n):
        # Queue will store tuples of (current number, step count)
        queue = deque([(n, 0)])
        # Set to track visited numbers to prevent revisiting
        visited = set([n])
        
        while queue:
            current, steps = queue.popleft()
            
            # If we reach 1, return the number of steps
            if current == 1:
                return steps
            
            # Apply the allowed operations
            if current % 2 == 0:
                next_num = current // 2
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))
            else:
                next_num1 = current + 1
                next_num2 = current - 1
                if next_num1 not in visited:
                    visited.add(next_num1)
                    queue.append((next_num1, steps + 1))
                if next_num2 not in visited:
                    visited.add(next_num2)
                    queue.append((next_num2, steps + 1))
              
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the size of the input number. At worst we will visit every number between n and 1 so the number of operations scales linearly.
O(n) space complexity since at worst we still store every number between n and 1 in the queue.

Strength(s):
- reinforces BFS concepts
- linear space and time complexity

Weakness(es):
- difficult to understand at first when reading
- to further reinforce class concepts, recursion with memoization could be used (all depends on what student is weakest at or goal of learning is)
"""

"""
Problem 2:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

U - Understand
1) Does output have to be a string or int?
2) Do we have to check input for proper Roman numerals formatting? (i.e. only up to 3 of a numeral)
3) Are there any cases where a numeral is smaller than the numeral comes after it and we should not reduce the value of the larger numeral? I.e. cases where V might come after I but not need to be reduced.

M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Stack - likely
Hashmap - likely
Recursion Memoization - likely

P - Plan
Write out in plain English what you want to do:
When manually converting roman numerals to integer, we can go in reverse order from right to left. For each numeral, we check if it is larger than the previous numeral (the numeral to the right of it when going in normal order).
If so, we add it to the total value. If the numeral is lesser than the previous numeral, we subtract it from the total value.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define the Roman numeral mappings
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize total and a pointer to track the previous value
        total = 0
        prev_value = 0
        
        # Traverse the string from right to left
        for char in reversed(s):
            value = roman_to_int[char]
            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                # Otherwise, add it to the total
                total += value
            # Update the previous value to the current value for the next iteration
            prev_value = value
        
        return total

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the size of the input numerals string since we process the string linearly from right to left in reverse order with constant time.
O(1) space complexity since only total_size and prev_value are updated and will use constant memory as an int.

Strength(s):
- human readable and intuitive, it is easy to understand what is happening in the code and lines up well with manual approach
- linear time complexity and constant space complexity

Weakness(es):
- could be recursion with memoization to reinforce learnings of this week's lesson
- passes all tests in leetcode but doesn't address any improperly formatted roman numerals
"""
