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

"""
Problem 2:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

U - Understand
1) Are we case sensitive when comparing strings? E.g. is ABC equivalent to abc?
2) Is input only alphabetical? Or can the strings contain other characters (e.g. numbers, punctuation, etc.)? Should we check for this in our input?
M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - unlikely
Arrays - likely
Linked List - unlikely
P - Plan
Write out in plain English what you want to do:
We can start with the first string as our prefix. Then, we can iterate through the rest of the strings in the input.
We compare the prefix with the equivalent length prefix of the string we are looking at.
If the characters are not equivalent, we shorten the prefix. We continue until an equivalent prefix is found.
If the prefix string becomes empty, then we return an empty string.
I - Implement
Translate the pseudocode into Python and share your final answer:
"""
def longestCommonPrefix(self, strs):
  # Edge case: if the list is empty, return an empty string
  if not strs:
      return ""
  
  # Start with the first string as the prefix
  prefix = strs[0]
  
  # Iterate through the remaining strings
  for string in strs[1:]:
      # Adjust the prefix by comparing with each string
      while string[:len(prefix)] != prefix and prefix:
          # Shorten the prefix by removing the last character
          prefix = prefix[:-1]
      
      # If prefix becomes empty, return an empty string
      if not prefix:
          return ""
  
  # Return the longest common prefix found
  return prefix

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n*m) time complexity where n is the number of strings and m is the length of the shortest string.
O(1) space complexity

Strength(s):
- human readable and intuitive, it is easy to understand what is happening in the code
- constant space complexity

Weakness(es):
- time complexity does not scale well for larger groups of strings
- we look at each string in the input array, comparing character by character
"""

"""
Problem 3:
Given two binary strings a and b, return their sum as a binary string.

U - Understand
1) Do we have a restriction on how long the resulting binary string can be?
2) Do we need to handle leading zeroes in the result?
M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - unlikely
Arrays - neutral
Linked List - likely
P - Plan
Write out in plain English what you want to do:
To add binary numbers, we start at the end of the string and sum character by character. If the sum of two characters >= 2, the resulting sum is sum % 2 with
a carry of sum // 2 (floor division of sum divided by 2).
So, we sum the numbers character by character moving backwards and make sure to keep track of the carry figure.
I - Implement
Translate the pseudocode into Python and share your final answer:
"""
def add_binary(a, b):
    # Initialize result string and carry
    result = []
    carry = 0

    # Pointers for a and b
    i, j = len(a) - 1, len(b) - 1

    # Iterate over both strings from the end
    while i >= 0 or j >= 0 or carry:
        # Get the current bit from a and b, or 0 if out of bounds
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        # Compute the sum of the bits and the carry
        total = bit_a + bit_b + carry

        # Compute the new bit and carry
        carry = total // 2  # Update carry for the next iteration
        result.appent(str(total % 2)  # append the resulting bit to result

        # Move the pointers to the next bits
        i -= 1
        j -= 1

    # The result is built in reverse order, so we need to reverse it
    return ''.join(reversed(result))

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the length of the longer string
O(n) space complexity

Strength(s):
- follows the same logic that we would use to compute the sum by hand so it is easy to follow

Weakness(es):
- appending (O(1)) at every step then reversing once (O(n)) is more efficient than inserting (O(n)) at every step but 
this may make the code harder to read / understand
- if using Java, can use string builder instead of a list for greater efficiency
"""
