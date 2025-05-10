"""
Example 2: 239. Sliding Window Maximum

Given an integer array nums and an integer k, there is a sliding window of size k that moves from the very left to the very right. For each window, find the maximum element in the window.

For example, given nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, return [3, 3, 5, 5, 6, 7]. The first window is [1, 3, -1, -3, 5, 3, 6, 7] and the last window is [1, 3, -1, -3, 5, 3, 6, 7]

Note: this problem is significantly more difficult than any problem we have looked at so far. Don't be discouraged if you are having trouble understanding the solution.
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from typing import List

from  collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    queue = deque()
    ans = []

    for i, num in enumerate(nums):
        while queue and nums[queue[-1]] < num:
            queue.pop()

        queue.append(i)

        if queue[0] + k == i:
            queue.popleft()

        if i >= k-1:
            ans.append(nums[queue[0]])

    return ans

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
