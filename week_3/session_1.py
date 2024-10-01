"""
Problem 1:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

- Understand
1) (Edge case) If the array is empty or only contains one height, what should we return?
2) Do we consider the bars in between the two bars we are looking at when we calculate the amount the container holds?

M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - likely
Arrays - unlikely
Recursion - unlikely

P - Plan
Write out in plain English what you want to do:
This is a classic two pointer maximization problem. We want to calculate the maximum area between two heights, multiplying the distance between the two heights by the lesser of the two heights.
So, in order to find the maximum, we start with left and right pointing to the leftmost and rightmost heights of the array, respectively.
We store the area as the maximum area if it is larger, then move the lesser of the two pointers inward. We continue until the pointers are touching.
Finally, we return the value of maximum area.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area with the current pair of lines
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the length of the input array.
O(1) space complexity

Strength(s):
- very space efficient (constant space complexity)
- linear time complexity
- easy approach to remember when seeing this problem again in future assessments or interviews

Weakness(es):
- doesn't specifically utilize the fact that the input comes in an array
"""

"""
Problem 2:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

U - Understand
1) (Edge case) Are we supposed to ignore punctuation and spaces in input strings?
2) Is there a limit to the length of input we are given?
3) Any constraints on what functions we can use? Time constraints?

M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - likely
Recursion - unlikely
Arrays - neutral

P - Plan
Write out in plain English what you want to do:
Filter out all the non alphanumeric characters. Lower the remaining characters so there is no case sensitive issues.
Reverse the string and compare that string with the original string. Return true if they are the same.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Normalize the string (remove non-alphanumeric characters and convert to lowercase)
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Step 2: Compare the normalized string with its reverse
        return filtered_chars == filtered_chars[::-1]
      
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the length of the input string
O(n) space complexity (since we store a copy of the reverse string)

Strength(s):
- human readable and intuitive, it follows a simple manual approach to the problem
- linear time & space complexity

Weakness(es):
- we can improve space complexity by using a two pointer approach
- approach may not be allowed in interview context (i.e. similar to reverse string problem, interviewer may be testing for familiarity with two pointer approach)
"""
