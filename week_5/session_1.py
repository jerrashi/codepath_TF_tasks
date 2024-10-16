"""
Problem 1:
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

- Understand
1) Will there be any cases where we need to retrieve calls more than t-3000 time ago?
2) Are there any restrictions we have for what data structures we can use?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Stacks - likely
Double ended queue - likely
Recursion - unlikely
Two Pointer - likely
Sliding Window - likely

P - Plan
While we can use a sliding window / two pointer or stack approach, it is more memory efficient to use a double ended queue.
Since we know that inputs will be strictly increasing, we can just append calls to a queue and popleft when the most recent call is greater than
the first call by more than 3000.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        # Add the new request to the queue
        self.requests.append(t)

        # Remove requests that are older than t - 3000 milliseconds
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of requests in the 3000ms window
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
O(1) time complexity for ping
O(n) space complexity where n is the length of the input since we only store the most recent pings

Strength(s):
- constant time complexity for ping
- space complexity will usually be better than O(n) since we remove pings from the queue regularly.

Weakness(es):
- we don't store the pings which may be a problem if this function is used differently in the future (or if we need to preserve a record of pings)

An alternative solution which is slightly less space efficient using a sliding window is attached below:
"""
class RecentCounter:
    def __init__(self):
        self.requests = []  # List to store request times
        self.start = 0      # Left pointer to keep track of valid requests

    def ping(self, t):
        # Add the new request time to the list
        self.requests.append(t)

        # Move the left pointer forward to discard old requests
        while self.requests[self.start] < t - 3000:
            self.start += 1

        # The number of valid requests is the size of the current window
        return len(self.requests) - self.start

"""
Problem 2:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue 
(push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long 
as you use only a stack's standard operations.

U - Understand
1) Do we have any time or space complexity constraints for each operation?
2) Are there any memory constraints to be aware of?

M - Match
List out 2-3 types of problems that we might consider and likelihood of match: Likely, Neutral, Unlikely. e.g. Linked List = Likely, Stack = Unlikely
Arrays - likely
Greedy - unlikely
Sorting - unlikely

P - Plan
Write out in plain English what you want to do:
A queue is a FIFO structure while a stack is a LIFO structure. Thus, if we use two stacks (using arrays in python), one for inputting data and one
for storing data to be output, we can simulate a queue.
The input array is what we append to. The output arrayr, populated using the transfer helper function, stores the input array in reverse.
For push, we simply append data to the end of the input array.
For pop, we pop (remove the last element) from the output array. If the output array is empty, we use the transfer helper function to move the
data from the input array to the output array. Then, we pop from the output array.
Similarly, for peek, we return the last element in the output array. If output array is empty, we transfer the contents of input array to output.

I - Implement
Translate the pseudocode into Python and share your final answer:
"""
class MyQueue:
    def __init__(self):
        self.input_stack = []  # Stack for incoming elements
        self.output_stack = []  # Stack for elements ready to be dequeued

    def push(self, x):
        """Push element x to the back of the queue."""
        self.input_stack.append(x)

    def pop(self):
        """Removes the element from the front of the queue and returns it."""
        # Transfer elements if output_stack is empty
        if not self.output_stack:
            self._transfer()
        return self.output_stack.pop()

    def peek(self):
        """Returns the element at the front of the queue."""
        # Transfer elements if output_stack is empty
        if not self.output_stack:
            self._transfer()
        return self.output_stack[-1]

    def empty(self):
        """Returns true if the queue is empty, false otherwise."""
        return not self.input_stack and not self.output_stack

    def _transfer(self):
        """Helper function to transfer elements from input_stack to output_stack."""
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

"""
RE - Review and Evaluate
Run your code. Evaluate the performance of your algorithm and share at least one strong/weak or future potential work.
Time:
push: O(1)
pop: O(1)
peek: O(1)
empty: O(1)

Space: O(n) where n is size of input

Strength(s):
- amortized constant time complexity for all operations

Weakness(es):
- we use a helper function, which may not be allowed by the interviewer or in an online assessment context
"""
