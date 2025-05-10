"""
Example 3: 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest subarray such that the absolute
difference between any two elements of this subarray is less than or equal to limit.
Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109
"""
from collections import deque
from typing import List

def longestSubarray(nums: List[int], limit: int) -> int:
    ans = 0
    increasing = deque()
    decreasing = deque()

    left = 0

    for right in range(len(nums)):
        while increasing and increasing[-1] > nums[right]:
            increasing.pop()

        while decreasing and decreasing[-1] < nums[right]:
            decreasing.pop()

        increasing.append(nums[right])
        decreasing.append(nums[right])


        while increasing and decreasing and decreasing[0] - increasing[0] > limit:
            if decreasing[0] == nums[left]:
                decreasing.popleft()
            if increasing[0] == nums[left]:
                increasing.popleft()

            left += 1

        ans = max(ans, right - left + 1) # length of window

    return ans

print(longestSubarray([8,2,4,7], 4))

