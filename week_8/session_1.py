
"""
Problem 1:
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the 
elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note 
that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number 
of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements
are emails in sorted order. The accounts themselves can be returned in any order.

- Understand
1) Are the email addresses sorted by alphabetical order?
2) Can there be multiple accounts with the same name but different email addresses?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Graphs - likely
Union Find - likely
DFS - likely

P - Plan
Write out in plain English what you want to do:
This problem is a classic example of connecting disjoint sets in a graph (similar to number of islands/provinces). If we were to graph the emails as
nodes in a graph, connected emails are emails belonging to the same account. When an email shows up in multiple connected sets, we can join the sets.
Therefore, we can implement it using Union Find, although personally I found the union find implementation more challenging to understand.
Therefore, I will first go through the DFS implementation. For DFS implementation, we need to build a few data structures:
1) email_graph - this is an adjacency list where the key and values are both email addresses. Each email address is connected to other email addresses
tied to the same account. For example, if given an account ["John", "johnsmith@gmail.com", "john_00@yahoo.com"] email_graph would look like
{
  "johnsmith@gmail.com" : ["john_00@yahoo.com"], 
  "john_00@yahoo.com" : ["johnsmith@gmail.com"]
}
2) email_to_name - a dictionary storing the name on the account associated with each email. For the same example prior, email_to_name looks like
{
  "johnsmith@gmail.com" : "John",
  "john_00@yahoo.com" : "John"
}
Once we have set up and populated those two data structures, we can run a slightly modified DFS on the graph. All we have to do is also append all 
visited emails from the starting email to a list that we will append to the account name and return.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    from collections import defaultdict

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # Step 1: Build the graph
        email_graph = defaultdict(list)
        email_to_name = {}
        
        # For each account, link all emails together and record the name
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_graph[first_email].append(email)
                email_graph[email].append(first_email)
                email_to_name[email] = name
        
        # Step 2: Perform DFS to find connected components
        def dfs(email, emails):
            visited.add(email)
            emails.append(email)
            for neighbor in email_graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, emails)
        
        visited = set()
        merged_accounts = []
        
        for email in email_graph:
            if email not in visited:
                # Collect all emails in the current connected component
                emails = []
                dfs(email, emails)
                # Sort emails and add the name at the beginning
                merged_accounts.append([email_to_name[email]] + sorted(emails))
        
        return merged_accounts

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(nlogn) time complexity since dfs is almost O(n) and we sort each list of emails before appending it to the results
O(n) space complexity since we store email_graph and email_to_name for each email address

Strength(s):
- utilizes DFS search

Weakness(es):
- have to create additional data structures, which may be hard to remember and may not be allowed by interviewer

Below is the Union Find Implementation:
"""
class Solution(object):
    from collections import defaultdict

    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.rank = {}

        def find(self, email):
            if self.parent[email] != email:
                self.parent[email] = self.find(self.parent[email])  # Path compression
            return self.parent[email]

        def union(self, email1, email2):
            root1 = self.find(email1)
            root2 = self.find(email2)
            
            if root1 != root2:
                # Union by rank
                if self.rank[root1] > self.rank[root2]:
                    self.parent[root2] = root1
                elif self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = self.UnionFind()
        email_to_name = {}

        # Step 1: Initialize Union-Find structure and map emails to names
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            # Make sure each email has an entry in Union-Find
            for email in account[1:]:
                if email not in uf.parent:
                    uf.parent[email] = email
                    uf.rank[email] = 0
                uf.union(first_email, email)  # Union all emails with the first email
                email_to_name[email] = name   # Map email to name

        # Step 2: Group emails by their root parent
        root_to_emails = defaultdict(list)
        for email in uf.parent:
            root_email = uf.find(email)
            root_to_emails[root_email].append(email)

        # Step 3: Format the result
        merged_accounts = []
        for emails in root_to_emails.values():
            name = email_to_name[emails[0]]
            merged_accounts.append([name] + sorted(emails))
        
        return merged_accounts

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
