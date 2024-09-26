"""
Problem 1
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

# Understand
Should we create a new array, which increases time complexity?
Is it ok to update the original shifts array?

# Match
String manipulation problem
Common string patterns:
Two pointers - likely
Sliding window - likely
Stacks - likely

# Plan
To convert the shifts (a number) to letters, we can use ord(c) in python, which converts letters/characters to ASCII encoding
eg) a = 26
For this problem, we can take one of two approaches:

Approach Number 1:
Iterative approach

for num, i in enumerate(shifts):
    for j in range(i + 1):
        shift(s[j]) num times
        
Approach Number 2:
Iterate from shifts from end to beginning
Add the shifts to get the total number of shifts at each index

Eg) shifts = [3, 5, 9]
Actual shifts operations: [17, 14, 9]

For this implementation, we will use approach 1. We will go through the shifts array and create a copy that contains the actual number of shifts
to perform at each index by summing the numbers in reverse order from end to beginning. For example, [1,2,3] becomes [6,5,3] since that is the
actual number of shifts to perform at each index. Then, we go through the copy of the shifts index we created and apply that number of shifts
to the letter at that index.
"""
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        """

        Test cases:
        Input: s="abc", shifts = [3, 5, 9]
        Output: "rpl"
        Shifts index 0 = 3:
        index 0 of string: a -> b -> c -> d
        index 1 of string: b unchanged
        index 3 of string: c unchanged
        s = "dbc"

        Shifts index 1 = 5:
        index 0 of string: d -> e -> f -> g -> h -> i
        index 1 of string: b -> c -> d -> e -> f -> g
        index 2 of string: c unchanged
        s = "igc"

        Shifts index 2 = 9:
        index 0 of string: i -> j -> k -> l -> m -> n -> o -> p -> q -> r
        index 1 of string: g -> h -> i -> j -> k -> l -> m -> n -> o -> p    
        index 2 of string: c -> d -> e -> f -> g -> h -> i -> j -> k -> l
        s = "rpl"   

        Input: s="aaa", shifts = [1, 2, 3]
        Output: "gfd"

        Edge case:
        "z" -> a
        input: s = "zzz", shifts = [1, 2, 3]

        shift 1:
        z - > a
        z
        z
        s = "azz"

        shift 2:
        a -> b - > c
        z -> a -> b
        z
        s = "cbz"

        shift 3:
        c -> d -> e -> f
        b -> c -> d -> e
        z -> a -> b -> c
        s = "fec"

        Step 1: Update the shifts array
        sum = 0
        for i in range(len(shifts) - 1, -1, -1):
            sum += shifts[i]
            shifts[i] = sum

        Step 2: perform shifts
        * double check range *
        res = ""
        for i in range(len(shifts)):
            res.append(shift(s[i], shifts[i]))

        Step 3: implement shift function
        def shift(c: char, num: int):
            sub step 1:
            we want to increment the unicode by num
            sub step 2:
            if unicode for c + num is > ord(z), then wrap araound
            sub step 3:
            convert unicode back to a letter
            c = (ord(c) + num)
            c = "z", which is 90
            "a" = 90 - 25 = 65
            shift it by 5
            c = 95 % 90 = 5

            c = 70
            
            if c > ord(z):
                c = ord(a) + (c % ord(z)) ??
            c = chr(c)
        """
        # Step 1: define shift function
        def shift(c, num):
            new_pos = (ord(c) - ord('a') + num) % 26
            return chr(ord('a') + new_pos)

        # Step 2: Update the shifts array
        sum = 0
        for i in range(len(shifts) - 1, -1, -1):
            sum += shifts[i]
            if sum >= 26:
                sum = sum % 26
            shifts[i] = sum

        # Step 3: perform shifts
        res = ""
        for i in range(len(shifts)):
            res += shift(s[i], shifts[i])
        # Step 4: return res
        return res
"""
Evaluate:
O(n^2) time complexity due to string concatenation
O(n) space complexity due to shifts array

Pros:
- human readable
- linear space complexity

Cons:
- the time complexity can be improved by changing to a list and then joining the list as a string. String concatenation requires copying every
string character first which adds to time complexity.
- space complexity can be improved by not using a shifts array. Instead, a total_sum variable can be used and the shifts array can be parsed from 
end to beginning, applying the shifts to the input string from end to beginning as well. This will also save from looping through the input array twice.
"""

"""
Problem 2:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Understand:
Do we have any time or space complexity constraints?
Can we modify the original zeroes in the matrix at all?

Match:
Array manipulation problem
Common patterns:
matrix manipulation - likely
stacks - unlikely
queues - unlikely

Plan:
We go through the array and record whether or not the first row or column has zeroes. Next, we iterate through the rest of the matrix (besides the
first column and first row) and record in the first row/column if there is a zero in that column/row. Lastly, we iterate through the first row and
column and for any indices that are 0, we set the corresponding row/column to 0. Lastly, we set the first column or row to 0 if we found a zero in 
the first column/row in the beginning.

"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def nullify_row(matrix, row_index):
            for j in range(len(matrix[0])):
                matrix[row_index][j] = 0
        
        def nullify_col(matrix, col_index):
            for i in range(len(matrix)):
                matrix[i][col_index] = 0
                
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            if matrix[i][0] == 0:
                nullify_row(matrix, i)

        for j in range(1, cols):
            if matrix[0][j] == 0:
                nullify_col(matrix, j)
        
        if first_row_has_zero:
            nullify_row(matrix, 0)

        if first_col_has_zero:
            nullify_col(matrix, 0)

"""
Evaluate:
O(n) time complexity, where n is the number of rows * number of cols
O(1) space complexity

Pros:
- intuitive in place manipulation of the data

Cons:
- iterates through the matrix multiple times
"""
        
        
        
