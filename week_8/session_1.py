
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
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals 
targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

U - Understand
1) Does the order of nodes returned matter?
2) Are all node values non-negative?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
BFS - likely
DFS - likely
Union Find - unlikely

P - Plan
Write out in plain English what you want to do:
For this problem, we can use DFS or BFS and store the sum along each path. When we reach the amount and are at a leaf node, we append the route we
took to the results.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Add the current node to the path
            current_path.append(node.val)
            current_sum += node.val
            
            # Check if we've reached a leaf node with the target sum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))  # Append a copy of the path
            
            # Recursively explore left and right children
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            
            # Backtrack
            current_path.pop()
        
        dfs(root, [], 0)
        return result
"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the number of nodes
O(h) space complexity where h is the height of the tree

Strength(s):
- linear time complexity

Weakness(es):
- space complexity doesn't scale as well
"""
