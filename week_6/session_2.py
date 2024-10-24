"""
Problem 1:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

- Understand
1) Are there any restrictions on import statements?
2) (Edge case) what do we return if given an empty matrix?
3) Are cities' connections always 2 ways? I.e. can city A be connected to city B but not the other way around?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Stacks - unlikely
Double ended queue - likely
BFS - likely
DFS - likely

P - Plan
This is very similar problem to the "Number of Islands" problem on leetcode and both of these problems can be solved using BFS or DFS. Essentially,
what we will do is iterate through cities. At each city, if we have not visited it before, we will increment the number of provinces by 1. Then, we
will conduct BFS or DFS to reach all connected cities and add those to the visited set. Lastly, we return the number of provinces.


I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    from collections import deque

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        provinces = 0

        def bfs(city):
            queue = deque([city])
            while queue:
                start = queue.popleft()
                for neighbor in range(n):
                    if isConnected[start][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        """
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        """

        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                bfs(i)
                #dfs(i)

        return provinces
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n2) time complexity where n is number of cities since we iterate through every city and then check for connections to every other city
O(n) space complexity since we store every visited city in the visited set

Strength(s):
- utilizes BFS/DFS search, which are commonly used graph algorithms

Weakness(es):
- O(n^2) time complexity
- union find is a more natural fit for this problem (but to be fair is a more complicated algorithm to remember)

Here is the union find implementation
"""
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution(object):

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):  # Only check upper triangle to avoid redundancy
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        # Count unique roots to determine the number of provinces
        return len(set(uf.find(i) for i in range(n)))

"""
Problem 2:
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

U - Understand
1) Are there any limitations on import statements, additional classes, etc. that we should be aware of?
2) (Edge case) What do we return if given an empty graph?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Double ended queue - likely
BFS - likely
Queues - likely
DFS - likely

P - Plan
Write out in plain English what you want to do:
This is another classic graph problem that can be solved with either a BFS or DFS approach. We will clone each node when we visit it by adding it
to the visited set and appending each neighboring node to the cloned node. Lastly, we return the visited set at the end.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        """
        def bfs(start):
            queue = deque([start])
            visited[start] = Node(start.val)  # Clone the starting node

            while queue:
                current = queue.popleft()

                # Iterate over all neighbors of the current node
                for neighbor in current.neighbors:
                    if neighbor not in visited:
                        # Clone the neighbor if not visited yet
                        visited[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)

                    # Add the cloned neighbor to the current node's neighbors list
                    visited[current].neighbors.append(visited[neighbor])
        
        if node:
            bfs(node)
            return visited[node]
        else:
            return None
        """
        
        return dfs(node) if node else None
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(V+E) time complexity where V is number of vertices and E is number of edges since we visit all vertices and traverse all edges
O(V) space complexity for visited dictionary and queue in BFS

Strength(s):
- O(m*n) time and space complexity (basically linear complexity)

Weakness(es):
- we store visited cells in a set and a queue, which uses more space than DFS
"""
