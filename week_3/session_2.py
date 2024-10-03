"""
Problem 1:
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of 
one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling 
time.

​Return the minimum number of intervals required to complete all tasks.

- Understand
1) (Edge case) If the cooling time is 0, do we return the length of input array?
2) Is the input case sensitive? I.e. is 'a' the same as 'A'?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Stacks - likely
Greedy - likely
Recursion - unlikely

P - Plan
Write out in plain English what you want to do:
When doing this problem manually, one possible approach would be to first count the frequency of each letter in the input array.
Next, we take the most common letter and repeat it over and over again with n spaces in between each number. We can store the # of times the most 
common letter appears as max_count. Thus, we would have (max_count - 1) blocks of (n + 1) size, plus 1 for the most commmon letter. 
For example, if we had 3 A's and n = 2, we would have 2 blocks of size 3 (A _ _ and A _ _) plus another A at the end.
When we include the frequency of the other letters, we realize that the minimum number of slots necessary to fit the given input array is 
(max_count - 1) * (n + 1) + max_count_tasks where max_count_tasks equals the number of tasks with a frequency equal to the most common letter.
Why is this the case? Well, if we have 2 letters (A & B) both with frequency 3 and then a letter (C) with frequency of 2, we know that we need 
(3 - 1) * (2 + 1) + 2 = 8 slots to fit everything. That is, we would have blocks A _ _ A _ _ then A B at the end. That is because the other letters
of the input array can fit into the max_count - 1 slots in between instances of the letter A. However, if they have as many instances as A, that
means they have to appear after A.
Lastly, we compare the length of the number of slots calculated with this formula with the original input length. If the input length is longer, that
means that it can not fit inside the slots that we calculated earlier and n is small enough that the total length required will just be the input 
length. For example, if we have an input of (A, A, A, B, B, B, C, C, D, D, E, E), that is 3 A's, 3 B's, 2 C's, 2 D's, and 2 E's, we have 12 
characters. Using the same formula as before, we would get 8 slots. This is not enough to fit the full array so instead we return 12, the lgnth of the
original input array.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    from collections import Counter

    def leastInterval(self, tasks, n):
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Get the maximum frequency
        max_count = max(task_counts.values())
        
        # Count how many tasks have this maximum frequency
        max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # Calculate the total number of slots needed
        total_slots = (max_count - 1) * (n + 1) + max_count_tasks
        
        # The minimum intervals required is the maximum of total slots or the number of tasks
        return max(total_slots, len(tasks))

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(m + k) time complexity where m is the number of tasks and k is the number of unique tasks. We have O(m) time complexity to iterate through the 
entire input array to create the counter, then O(k) time complexity to iterate through the counter (which is structured as a letter: frequency
dictionary) to find the maximum.
O(k) space complexity where k is the number of unique tasks. Again, we have a counter which stores data as a letter: frequency dictionary so it will
scale in size proportional to the number of unique tasks.

Strength(s):
- very space efficient (linear space complexity)
- mostly linear time complexity
- math trick that can be memorized for later use when seeing this problem again in future assessments or interviews

Weakness(es):
- if interviewer/assessment doesn't allow use of counter function, you can manually implement as follows:
"""
tasks_count = {}
for task in tasks:
  tasks_count[task] = tasks_count.get(task, 0) + 1
  
max_count = max(tasks_count.values())
    
max_count_tasks = 0
for count in tasks_count.values():
    if count == max_count:
        max_count_tasks += 1
"""
Problem 2:
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one 
unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not 
considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no 
bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical 
line.

U - Understand
1) We want to minimize the number of bricks that we "cross through" by maxmizing the number of break edges we touch, correct?
2) Do we have any constraints on built in functions, time/space complexity that we have to be aware of?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Dictionary - likely
Recursion - unlikely
Greedy - neutral

P - Plan
Write out in plain English what you want to do:
Similar to problem 1, we can use some math tricks gleaned from a manual approach to find the solution. When doing this by hand, we can find the 
number of edges at each position in the row. For example, in the example, there are two edges at position 1 in the wall (1 and 1 bricks on the 
bottom), two edges at position 2 (2 brick in the second row and second 1 brick in the bottom row), etc.
Then, to find the minimum number of bricks to cross, we subtract the maximum number of edges at any position from the length of the wall (i.e. 
number of rows).

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge_counts = {}  # Dictionary to count edge positions

        for row in wall:
            position = 0  # Initialize the starting position for each row
            # Exclude the last brick to avoid counting the wall's right edge
            for brick in row[:-1]:
                position += brick
                edge_counts[position] = edge_counts.get(position, 0) + 1  # Increment the count for this edge position
        
        # Edge case - there are no edges (all rows have a single brick), the line must cross all bricks
        if not edge_counts:
            return len(wall)
        
        # Find the position with the maximum number of aligned edges
        max_edges = max(edge_counts.values())
        
        # The minimum number of bricks crossed is the total number of rows minus the maximum aligned edges
        return len(wall) - max_edges
      
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(m + k) time complexity where m is the number of bricks and k is the unique number of positions with edges. This simplifies to O(m) since m >= k 
(each position will require at least one brick so there is never a case where there are more positions than bricks).
O(k) space complexity where k is the unique number of positions with edges (since we store a dictionary of position: # of edges)

Strength(s):
- human readable and intuitive, it follows a simple manual approach to the problem
- linear time & space complexity

Weakness(es):
- relies on math tricks to understand what is happening
"""
