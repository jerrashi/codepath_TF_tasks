"""
Problem 1:
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

U - Understand
1) (Edge case) If the list is empty or only contains one node, what should we return?
2) When we make a copy of the nodes, is the copy an independent copy or a deep copy? I.e. does changing the next pointer of a node change a copy
of the node or the original node?

M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - likely
Arrays - unlikely
Recursion - unlikely
P - Plan
Write out in plain English what you want to do:
Using an approach similar to a two pointer approach for string reversal, we create a dummy node whose next points to the head node of our list.
We create another variable prev which points to the same node as dummy at first. Then, we iterate through our list. At each iteration, we
make the prev node point to the second node. This makes the second node first in that sequence instead. I.e. dummy -> 1 is changed to dummy -> 2.
Next, we make the first node point to the next node of the second node. I.e. 1 -> 2 is changed to 1 -> 3. Lastly, we change the next of the second
node to make to the first node. I.e. 2 -> 3 is changed to 2 -> 1.
The end result is dummy -> 1 -> 2 -> 3 -> 4 is changed to dummy -> 2 -> 1 -> 3 -> 4.
We iterate through the linked list like this until we reach the end and return dummy.next.
I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        # Dummy node to handle the head swap case easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the length of the linked list.
O(1) space complexity

Strength(s):
- very space efficient
- linear time complexity

Weakness(es):
- not very human readable, although it logically follows how one would manually swap nodes in a linked list by hand, the pointer logic is hard to
follow and can be error inducing to implement
"""

"""
Problem 2:
Given the head of a linked list, rotate the list to the right by k places.

U - Understand
1) Can we rotate a list more than the length of the list? Do we circle around if so?
2) (edge case) If k is 0 or the list is empty, what do we return?
M - Match
List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Pointer Bookkeeping = Likely
Two pointer - likely
Recursion - unlikely
Arrays - neutral
P - Plan
Write out in plain English what you want to do:
To manually rotate the list by hand, we could link the last node to the first node, creating a circular chain. Then we rotate however many times to
the right is necessary (k rotations = k % length rotations to save time) and lastly "cut" the chain by removing the link between the last node and
first node.
I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Base cases: empty list or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute the length of the list and get the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make the list circular
        tail.next = head

        # Step 3: Calculate the number of steps to the new head
        # Rotate by k % length to avoid unnecessary rotations
        k = k % length
        steps_to_new_head = length - k

        # Step 4: Find the new tail and new head
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Step 5: Break the circular link
        new_tail.next = None

        return new_head

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(n) time complexity where n is the length of the input linked list (although we traverse the list twice, O(n + n) simplifies to O(n))
O(1) space complexity

Strength(s):
- human readable and intuitive, it follows a simple manual approach to the problem
- linear time complexity
- constant space complexity

Weakness(es):
- we iterate through the list twice, so this may not be the most absolute time efficient solution
"""
