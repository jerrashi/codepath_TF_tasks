
"""
Problem 1:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all 
the n nodes to receive the signal, return -1.

- Understand
1) If we are given an empty network or network of only one node, what do we return?
2) Are we allowed to modify the input? Can we store additional data in a new data structure (i.e. a queue)?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Topological sort - unlikely
BFS - likely
DFS - unlikely
Dijkstra's - likely

P - Plan
In this problem, we are finding the shortest path to a given node in a graph with weighted edges. This is a classic Dijkstra's algorithm problem.
In Dijkstra's algorithm, we create a priority queue / minheap and set a distance dictionary corresponding to each node, defaulting to infinite value.
While the queue exists, we pop from the queue and for each neighbor of the popped node, we check if the current_distance + weighted distance to 
reach the new node is less than the current value in the dictionary. If it is, then we have found a shorter path and update the dictionary. We keep
doing this until we reach all nodes or the queue is empty.
Lastly, we return the maximum value of the distance dictionary to find the "farthest" node that will take the longest to reach the signal from our
starting node.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    import heapq
    from collections import defaultdict

    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Initialize min-heap and distances dictionary
        min_heap = [(0, k)]  # (distance, node)
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        
        # Step 3: Process nodes in order of the shortest distance
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)
            
            # If the distance is greater than the recorded distance, skip
            if curr_dist > distances[u]:
                continue
            
            # Step 4: Relax the edges
            for v, w in graph[u]:
                if curr_dist + w < distances[v]:
                    distances[v] = curr_dist + w
                    heapq.heappush(min_heap, (distances[v], v))
        
        # Step 5: Calculate the maximum distance in the distances dictionary
        max_dist = max(distances.values())
        return max_dist if max_dist < float('inf') else -1

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O((V+E)logV) time complexity where V is the number of nodes and E is the number of edges
O(V+E) space complexity since what takes up the most space is the adjacency list

Strength(s):
- utilizes Dijkstra's algorithm, a key graph algorithm

Weakness(es):
- have to import defaultdict and heapq structure, which may not be allowed by interviewer
"""

"""
Problem 2:
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different 
vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, 
bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs 
last in the input.

U - Understand
1) What do we do if we are given an empty graph? Or a graph with only one node?
2) What determines if an edge occurs "last" in the input?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Union Find - likely
BFS - unlikely
DFS - unlikely

P - Plan
Write out in plain English what you want to do:
This is a classic union find problem - cycle detection. We want to detect when the cycle is created in the graph and basically "undo" that cycle by
removing the edge so we have an acyclic graph / tree.
In union find, we set every node's parent to itself and then maintain a rank of each node, set to 1. We process the edges using unionfind: we "find"
the parent of each node, if they are equal to each other we return false since we have a cycle, and if they have different parents and different ranks,
we set the parent of the node with lower rank to the parent of the node with higher rank and increase the rank of the node with higher rank. If the
ranks are equal, we set the first node to be the parent of the second and increase the rank of said first node.
We loop through the input edges until we get a false value, which means a cycle was detected, and return that edge.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
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
            
            if rootX == rootY:
                return False  # x and y are already connected, so this edge forms a cycle
            
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            
            return True
    
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        uf = self.UnionFind(n + 1)  # +1 because nodes are 1-indexed

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        
        return []
        
        
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is number of edges
O(n) space complexity

Strength(s):
- reinforces uses of union find approach
- O(n) time and space complexity

Weakness(es):
- have to memorize union find implementation to use this code
"""
