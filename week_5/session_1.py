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
