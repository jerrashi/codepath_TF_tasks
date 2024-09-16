"""
Problem 1:
Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

U - Understand
1) (Edge case) If the two strings are the same, should we return true?
2) (Edge case) If the second string is empty, should we return true? If the first string is empty, should we always return false? What if both strings are empty?
M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - likely
Arrays - likely
Linked List - unlikely
P - Plan
Write out in plain English what you want to do:
One approach, using the two pointer approach, is to initialize p1 and p2 to the beginning characters of string 1 and 2. While p1 and p2 do not point to equivalent 
characters, we iterate p1 through the rest of the string until we either reach an equivalent character to p2 or the end of the first string.
If we reached the end of the first string, we return false. If we reached an equivalent character to p2, we iterate p1 and p2 as long as both point to equivalent 
characters. If we reach the end of string 2, return true since a match was found. If the two strings point to un-equivalent characters, then we iterate p1 and 
reset p2 to the beginning of the second string. We continue until we reach the end of string 1 or a match is found.
I - Implement
Translate the pseudocode into Python and share your final answer:
"""
def substring(large_str, potential_substr):
  # store lengths of strings
  large_len = len(large_str)
  substr_len = len(potential_substr)
  
  # edge case - potential substring is empty
  if substr_len == 0:
    return True

  # edge case - potential substring is longer than first string
  if substr_len > large_len:
    return False
    
  # iterate through large string up until length of substring
  for i in range(large_len - substr_len + 1):
        # Initialize two pointers
        p1 = i
        p2 = 0
        
        # compare characters while they are equivalent
        while p2 < substr_len and large_str[p1] == potential_substr[p2]:
            p1 += 1
            p2 += 1
        
        # If we've checked the entire second string, we found a match
        if p2 == len(s2):
            return True
    
    # If no match is found after the loop, return False
    return False

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n*m) time complexity where n is the length of the large string and m is the length of the potential substring.
O(1) space complexity

Strength(s):
- human readable and intuitive, it is easy to understand what is happening in the code
- constant space complexity

Weakness(es):
- time complexity does not scale well for larger strings
- more complex approaches such as KMP (Knuth-Morris-Pratt) or Rabin-Karp algorithm could scale better for larger strings.
"""
