"""
Problem 1:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

- Understand
1) (Edge case) What do we return if given an empty tree or a tree with only one node?
2) Are there any restrictions on creating additional data structures for this problem?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
BFS - likely
DFS - likely
Arrays - unlikely

P - Plan
This is a classic BFS / DFS problem and I will illustrate both approaches below.
In BFS (iterative), we create a queue and start with the root note. We add all children of the root node to the queue to be visited. Then, we popleft from the
queue and visit that node, appending all children who have not been visited to the queue. We continue until we traverse the whole tree/graph. In
this case, we store the depth level of each child reached and check if it is a leaf node. If it is, we return the depth. Since BFS traversal 
traverses the entire level before moving on to the next level, we know that the first leaf node we find will be the minimum depth leaf node.

In DFS (recursive), we create a set to store visited nodes. Given a root node, we perform DFS on each child node, checking first that they have not
been visited already. We keep going until every node has been reached. In contrast to BFS, we return the minimum depth of the left and right child 
nodes. This is because DFS will traverse a pathway to a leaf node first, then backtrack. Thus, the first leaf node we find may not be at the 
minimum depth.

I - Implement
Translate the pseudocode into Python and share your final answer:
BFS:
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    from collections import deque

    def minDepth(self, root):
        if not root:
            return 0

        # Initialize a queue for BFS
        queue = deque([(root, 1)])  # (node, depth)

        while queue:
            node, depth = queue.popleft()

            # Check if this is a leaf node
            if not node.left and not node.right:
                return depth

            # Add the children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

"""
DFS:
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def minDepth(self, root):
        if not root:
            return 0

        # If one of the children is None, we need to take the depth of the other child
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children are present, take the minimum of the two depths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
BFS:
O(n) time & space complexity where n is the total number of nodes in the input
DFS:
O(n) time & O(h) space complexity where n is the total number of nodes in the input, h is the height of the tree

Strength(s):
- linear time & space complexity

Weakness(es):
- dfs takes up O(h) space due to recursive calls but can be easier to understand
"""

"""
Problem 2:
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

U - Understand
1) How much do we remove if a treee does not contain 1?
2) Are there any memory constraints to be aware of?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
DFS - likely
Greedy - unlikely
Sorting - unlikely

P - Plan
Write out in plain English what you want to do:
A subtree does not contain a 1 if it's child nodes does not contain a 1 and it's node value does not equal 1.
Using a DFS approach, we can implement a helper recursive containsOne function. If the left or right child does not contain 1, then we set the left
or right child to None to delete it from the node. Then, we return True if the node == 1 or the left or right child contains 1.

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
    def pruneTree(self, root):
        # Helper function to perform post-order traversal
        def containsOne(node):
            if not node:
                return False  # Base case: empty node doesn't contain a 1
            
            # Recursively prune left and right subtrees
            left_contains_one = containsOne(node.left)
            right_contains_one = containsOne(node.right)

            # If a subtree doesn't contain a 1, remove it (set it to None)
            if not left_contains_one:
                node.left = None
            if not right_contains_one:
                node.right = None

            # Return True if the current node or any of its subtrees contain a 1
            return node.val == 1 or left_contains_one or right_contains_one

        # Use the helper function to determine if the root should be kept
        return root if containsOne(root) else None        

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity
O(h) space complexity where h is height of tree

Strength(s):
- linear time complexity
Weakness(es):
- BFS & DFS are usually interchangeable solutions in tree problems, however, since BFS processes trees in a level by level manner, the BFS approach
is less intuitive. We would have to process in a reverse level order, starting at leaf nodes first and then work our way up the tree.
"""
