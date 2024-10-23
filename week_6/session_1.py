"""
Problem 1:
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

- Understand
1) What is the distance between diagonal cells? I.e. the distance between a 0 at [0][0] and a 1 at [0][1]?
2) Are we allowed to modify the input matrix? Can we store additional data in a new data structure (i.e. a queue)?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Stacks - unlikely
Double ended queue - likely
BFS - likely
DFS - unlikely

P - Plan
This is a classic BFS problem - we are finding the shortest distance between two "nodes" (cells in this case) in a "tree" (matrix in this case). 
DFS is good for finding the shortest distance between two points since we search in a "layer" by "layer" manner. DFS, in contrast, is good for
determining whether a path exists between two nodes but not as good for finding the shortest distance.
In this approach, we will create a new distance matrix (the same size as the input matrix) to track the distance of each cell from its nearest 0.
We will populate this distance matrix with an extremely large value (inf) at each cell or a 0 if the original cell is a 0. We add all the cells
containing 0 to the queue to undergo BFS. In our BFS portion, we pop from the queue and explore all 4 neighbors. If the neighbor is in bound and
the distance value stored there is greater than the distance of the cell we explored from + 1, this means we have either found a shorter path to
a 0 from the cell or the cell contains a 1. Thus, we update the distance matrix for that cell to be distance of original cell + 1, then enqueue
the cell to the queue. We repeat this until the queue is empty and return the distance matrix.


I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    from collections import deque

    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        # Initialize the result matrix with large numbers (infinity).
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        # Enqueue all cells containing 0 and set their distance to 0.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        # Directions for moving up, down, left, right.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS.
        while queue:
            x, y = queue.popleft()
            # Explore neighbors.
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If the neighbor is within bounds and we find a shorter path, update it.
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        return dist

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(m*n) time complexity where m is number of rows and n is number of columns since we traverse the matrix to find 0s 
and (worst case scenario) traverse the whole matrix again in BFS
O(m*n) space complexity since we store a copy of the matrix

Strength(s):
- utilizes BFS search, which makes sense since we are searching for shortest paths

Weakness(es):
- traverse the matrix twice (first to find 0s, then to BFS)
- could be more intuitive
"""

"""
Problem 2:
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also 
given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or 
vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color 
of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

U - Understand
1) Do we worry about diagonal connections?
2) What do we do is original color is equal to new color?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Double ended queue - likely
BFS - likely
Stacks - likely
DFS - likely

P - Plan
Write out in plain English what you want to do:
This is a classic graph problem that can be solved with either a BFS or DFS approach. A BFS approach searches layer by layer for connected cells.
A DFS approach goes to the end of a direction first, then backtracks to find connected cells. I will implement a BFS approach since this is more
intuitive for me, personally, then go into a DFS approach.

For the BFS approach, we create a queue and attach the original cell we are looking at to the queue. We store the original color of this cell.
We create a set called visited and store the original cell to visited so we don't visit it again. In the BFS portion, we pop from the queue. 
We update the cell's value to the new color. We look at all four directions from the cell. If a new cell we are looking at is within bounds,
is not in visited, and equals the original cell color, we add it to the queue. Then we repeat. Lastly, we return the newly updated matrix.

I - Implement
Translate the pseudocode into Python and share your final answer:
BFS approach
"""
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # store the original color
        original_color = image[sr][sc]

        # edge check - make sure new color != original color
        if original_color != color:
            from collections import deque
            queue = deque()
            queue.append((sr, sc))
            visited = set()
            
            while len(queue) > 0:
                node = queue.popleft()
                row, col = node
                if node not in visited and image[row][col] == original_color:
                    visited.add(node)
                    image[row][col] = color
                    # check all four directions
                    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
                    for row_add, col_add in directions:
                        r = row + row_add
                        c = col + col_add
                        # check if the new cell is in bounds
                        if -1 < r < len(image) and -1 < c < len(image[0]):
                            if (r, c) not in visited and image[r][c] == original_color:
                                queue.append((r, c))
        return image
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(m*n) time complexity where m is number of rows and n is number of columns since worst case we visit every cell
O(m*n) space complexity where m is number of rows and n is number of columns since worst case we store very cell in
visited and/or queue

Strength(s):
- O(m*n) time and space complexity (basically linear complexity)

Weakness(es):
- we store visited cells in a set and a queue, which uses more space than DFS

Here is the DFS approach:
"""
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, there's nothing to do.
        if original_color == color:
            return image
        
        def dfs(row, col):
            # Base case: if out of bounds or not the original color, return.
            if (row < 0 or row >= len(image) or
                col < 0 or col >= len(image[0]) or
                image[row][col] != original_color):
                return
            
            # Change the color of the current pixel.
            image[row][col] = color
            
            # Recursively apply the flood fill on the 4 adjacent pixels.
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left
    
        # Start the flood fill process from the given starting pixel.
        dfs(sr, sc)
        
        return image
