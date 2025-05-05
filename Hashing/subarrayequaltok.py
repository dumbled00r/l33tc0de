"""
Example 4: 560. Subarray Sum Equals K

Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
"""
from collections import defaultdict


# example, k = 3, nums = [1, 2, 1, 2, 1]
def subarraySum(nums, k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0 # curr --> prefix sum

    for num in nums:
        curr += num
        ans += counts[curr-k]
        counts[curr] += 1
    return ans

subarraySum([-1, -1, 1], 0)