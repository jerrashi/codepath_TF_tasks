"""
Problem 1:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same 
letter cell may not be used more than once.

- Understand
1) Can the words be formed by diagonal movements? Or only horizontal/vertical?
2) Can words be formed using letters we have already visited? I.e. could a world loop around the map to go back to a previously visited letter?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Graphs - likely
DFS - likely
Backtracking - likely

P - Plan
Write out in plain English what you want to do:
This problem is a classic example of a backtracking algorithm. If we think about the problem intuitively/manually, we would look through the grid 
cell by cell, letter by letter. At each cell, we would check if it matches the first letter of the word we are looking for. If it does, we will keep
going and look at the neighboring cells. Once we find the letters that match with what letter we are looking for, we keep going until we have found
the whole word, and then return true. If we traverse the whole grid and don't find the word, then we return false.
To implement this in code, we write a dfs function. We will run the dfs at every cell in the grid by iterating over all the columns and arrays. If
the cell we are at does not match the letter in the word we are looking for, we return false. Otherwise, mark the cell as visited and then we perform
depth first search and look through every neighboring cell.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # Base case: if index matches the length of the word, we've found the word
            if index == len(word):
                return True
            # Check for out of bounds or mismatch
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited by storing its original value and setting it to a sentinel value
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all four directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )
            
            # Unmark the cell (backtrack)
            board[r][c] = temp
            return found

        # Try to start DFS from each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):  # Start DFS from (r, c) with index 0 of word
                    return True
        return False

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(m*n*4^L) time complexity where m is number of rows and n is number of columns and L is the length of the word we are looking for
O(L) space complexity where L is the length of the word we are looking for

Strength(s):
- utilizes DFS search and backtracking, two key concepts of this week's lecture

Weakness(es):
- we modify then revert the grid to save space but we might not be allowed to modify the input by the interviewer
"""

"""
Problem 2:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

U - Understand
1) Does the order of parentheses returned matter?
2) Are all node values non-negative?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
BFS - unlikely
DFS - unlikely
Backtracking - likely

P - Plan
Write out in plain English what you want to do:
For this problem, we can use a backtracking approach. If we think about the problem intuitively/manually, we can have an open or close parentheses 
at each position after the first. What are the requirements of each possibility? We need to have less open parentheses than the number we are 
generating parentheses for to add an open parentheses. We need to have more open parentheses than closed parentheses to add a closed parentheses.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s='', open_count=0, close_count=0):
            # Base case: when the length of the string reaches 2*n, add it to results
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # If the number of open parentheses is less than n, we can add an open parenthesis
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            # If the number of close parentheses is less than the number of open parentheses, we can add a close parenthesis
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        result = []
        backtrack()
        return result
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
 O(4^n / sqrt(n)) time complexity where n is the input numbers. There are 2^n possible paths but not all paths are valid so instead we use the nth
 Catalan number.
 O(4^n / sqrt(n)) space complexity if we consider the space for result (since there are 4^n/sqrt(n) valid paths). If we are only considering the 
 memory needed for the stack, we recurse up to a depth of O(2n) (since we will be configuring 6 parenthese for 3, and so onwhich simplifies to O(n).

Strength(s):
- showcases backtracking in a simple and easy to understand way

Weakness(es):
- time complexity is confusing to grasp
"""
