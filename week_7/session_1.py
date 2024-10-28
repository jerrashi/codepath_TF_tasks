
"""
Problem 1:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to 
finish all courses, return an empty array.

- Understand
1) Can a single course have multiple pre-requisites? Can a single course be a pre-requisite for multiple classes?
2) Are we allowed to modify the input? Can we store additional data in a new data structure (i.e. a queue)?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Topological sort - likely
BFS - likely
DFS - likely

P - Plan
Essentially, in this problem we are given a graph (or rather the edges and we have the process this input to construct the graph) and we are tasked
with finding if there is a valid path through this graph or not. This can be done with topological sorting, which is implemented with BFS or DFS.
Using BFS approach, known as Kahn's Algorithm, we start by iterating through the input to store the "indegree" of each node (i.e. the number of 
pre-requisites each class has) and the connections of each node (beginning node: ending node) in two separate hashmaps. Now that we have these two
hashmaps, we can start topological sort BFS style by starting at the first node in the "indegree" hashmap that has an indegree of 0. We "remove" that
node from the graph by decrementing every connected node recorded in the connections hashmap. We continue by looking for the next node that has an
indegree of 0 and we repeat the cycle until every node has been visited (meaning there is a valid path) or there are no nodes that can be visited but
there are still nodes remaining (meaning there is no valid path to visit all nodes).

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    from collections import deque, defaultdict

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Create the graph and compute in-degrees
        in_degree = [0] * numCourses
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        # Step 2: Initialize the queue with courses having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        # Step 3: Process the queue
        while queue:
            course = queue.popleft()
            result.append(course)

            # Reduce the in-degree of neighboring courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses were processed
        if len(result) == numCourses:
            return result
        else:
            return []  # Cycle detected, return empty array

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(V+E) time complexity where V is the number of courses and E is the number of pre-requisites since we visit each course and pre-requiste once
O(V+E) space complexity since we store a hashmap of every node's in-degree number and a hashmap of the connections of each node

Strength(s):
- utilizes BFS search and topological sort, two key concepts of graphs

Weakness(es):
- have to import defaultdict structure, which may not be allowed by interviewer

Below is the DFS implementation. Instead of a queue, we use an array to mark each node as visited, not visited, or visiting. We basically DFS 
traverse the entire graph (if possible) and if no loop is detected, we return the traversal order in reverse to get the topologically sorted array.
"""
class Solution(object):
    from collections import defaultdict
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the graph as an adjacency list
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        # Step 2: Initialize the visited array and result stack
        visited = [0] * numCourses  # 0 = unvisited, -1 = visiting, 1 = visited
        result = []
        
        # Step 3: Define the DFS function
        def dfs(course):
            if visited[course] == -1:  # Cycle detected
                return False
            if visited[course] == 1:  # Already processed
                return True

            # Mark the course as visiting
            visited[course] = -1

            # Visit all neighbors (dependent courses)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False  # Cycle detected in recursion

            # Mark the course as visited and add it to the result
            visited[course] = 1
            result.append(course)
            return True

        # Step 4: Perform DFS for all unvisited nodes
        for i in range(numCourses):
            if visited[i] == 0:  # If not yet visited
                if not dfs(i):
                    return []  # Cycle detected, no valid order

        # Step 5: Return the result in reverse order
        return result[::-1]  # Reverse to get the correct order

"""
Problem 2:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a 
prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course 
vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

U - Understand
1) What do we do if we are given an empty array?
2) Will this graph have cycles?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Topological sort - likely
BFS - likely
DFS - likely

P - Plan
Write out in plain English what you want to do:
For this problem, we can also use topological sort in a similar approach to the first question. Instead of returning a sorted array of the graph,
though, we will create a pre-requisite map of each course that takes into account courses further down the road. For example, if A is a pre-requisite
of B, we will add A to the pre-requisites map for B but also for C if B is a pre-requisite for C. Then, we will check is A is a pre-requisite of C
by checking if it is in the set of pre-requisites for C when we need to check each query.

I - Implement
Translate the pseudocode into Python and share your final answer:
BFS approach
"""
class Solution(object):
    from collections import defaultdict, deque

    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Step 1: Initialize adjacency list and prerequisites map
        indegree = [0] * numCourses
        adj = defaultdict(set)  # Adjacency list (graph)
        prerequisitesMap = defaultdict(set)  # Stores all prerequisites for each course

        # Step 2: Build the graph and calculate indegrees
        for [course, pre] in prerequisites:
            adj[course].add(pre)
            indegree[pre] += 1

        # Step 3: Initialize the queue with courses having zero indegree
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # Step 4: Perform BFS to populate the prerequisitesMap
        while queue:
            node = queue.popleft()
            for next_course in adj[node]:
                # Add current node and its prerequisites to the next course's prerequisite set
                prerequisitesMap[next_course].add(node)
                prerequisitesMap[next_course].update(prerequisitesMap[node])

                # Decrease the indegree and add to the queue if it becomes 0
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Step 5: Answer the queries using the prerequisitesMap
        result = []
        for u, v in queries:
            result.append(u in prerequisitesMap[v])

        return result
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(V+E) time complexity where V is the number of classes and E is the number of pre-requisites
O(V^2) space complexity since we store pre-requisites transitively for each class

Strength(s):
- reinforces topological sort approach

Weakness(es):
- O(V^2) space complexity gets unwieldy for larger inputs
"""
