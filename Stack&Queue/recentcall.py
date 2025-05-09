"""
Example: 933. Number of Recent Calls

Implement the RecentCounter class. It should support ping(int t), which records a call at time t,
and then returns an integer representing the number of calls that have happened in the range [t - 3000, t].
 Calls to ping will have increasing t.
"""
from collections import deque

class RecentCounter:
    def __init__(self):
        self.currqueue = deque()
        pass
    def ping(self, t: int) -> int:
        # this is to check
        while self.currqueue and  t - self.currqueue[0] > 3000:
            self.currqueue.popleft()
        self.currqueue.append(t)
        return len(self.currqueue)

if __name__ == "__main__":
    recentcounter = RecentCounter()
    ans = []
    data = [1, 100, 3001, 4000]

    for _ in data:
        ans.append(recentcounter.ping(_))
    print(ans)