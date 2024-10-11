"""
Problem 1:
Given a string s, find the length of the longest substring without repeating characters.

- Understand
1) (Edge case) If there is a tie between longest substrings, does it matter which substring we look at?
2) Is the substring case sensitive? Will we need to consider numbers or punctuation at all or only letters?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Stacks - likely
Greedy - unlikely
Recursion - unlikely
Two Pointer - likely
Sliding Window - likely

P - Plan
Using a two pointer approach, we have a left and right pointer. We increase the right pointer each iteration and check to see if it points to a letter already in our dictionary of characters.
If it does, then we point the left pointer to the left of the rightmost occurrence of the right pointer letter. Then, we update the value of the right pointer letter in the dictionary to the 
right pointer index to reflect the rightmost occurence of the letter. We update max_length and continue until we have iterated through the whole string.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to the right of the last occurrence of s[right]
            left = char_index[s[right]] + 1
        
        # Update the last seen index of the character at right pointer
        char_index[s[right]] = right
        
        # Calculate the window size and update max_length if it's the largest found
        max_length = max(max_length, right - left + 1)

    return max_length

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the length of the string.
O(m) space complexity where m is the number of distinct letters in the string.

Strength(s):
- increased (absolute) time efficiency compared to using a set since we can update left pointer in a single operation and constant time
- shows mastery of dictionary data structures

Weakness(es):
- uses additional memory to store the dictionary and the dictionary can get quite large if we extend the solution to larger character sets (numbers, punctuation, full ASCII, etc.)
"""

"""
Problem 2:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

U - Understand
1) Do we have to return the original strings or is it ok to return a list of copy of the strings?
2) Are there any memory constraints to be aware of?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Dictionary - likely
Recursion - unlikely
Greedy - neutral
Sorting - likely

P - Plan
Write out in plain English what you want to do:
One approach is to sort the each string alphabetically. Then, we can store the original string as the value and the sorted string as the key in a hashmap. We can add additional strings to the 
values if they have the same sorted string as a nother. However, the downside of this approach is that it take O(n(logn)) time complexity to sort each string.
Thus, we can instead use a counting operation at each string since counting takes O(n) time and store the key as a hashmap of the number of each letter found in the string. Similarly, we use
a hashmap and the value is the original string. We return the values of the hashmap to get our answer.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()
      
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n * k) time complexity where n is the number of strings and k is the length of each string.
O(n * k) space complexity where n is the number of strings and k is the legnth of each string

Strength(s):
- better time complexity than sorting solution (O(n*K) vs O(n*k*logk) time complexity)

Weakness(es):
- we use an array of length 26 even for short strings, which means space efficiency is worse for cases where we have few strings of short length (lots of wasted space in array)
- space complexity gets worse if scaled to include numbers, ASCII, etc.
- interviewer may not allow use of dictionaries or be concerned about space complexity
"""
