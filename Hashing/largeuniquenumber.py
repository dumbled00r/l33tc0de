"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
"""
from collections import defaultdict


def largestUniqueNumber(nums) -> int:
    # arr = [-1] * 2001
    # seen = defaultdict(int)
    # for i in range(len(nums)):
    #     seen[nums[i]] += 1
    #     if arr[nums[i]] == -1:
    #         arr[nums[i]] = 1
    #     else:
    #         arr[nums[i]] += 1
    #
    # for i in range(len(arr)-1, 0, -1):
    #     if arr[i] == 1:
    #         return i
    # return -1

    seen = defaultdict(int)
    for num in nums:
        seen[num] += 1

    arr = []
    for key, val in seen.items():
        if val == 1:
            arr.append(key)
    return max(arr) if arr != [] else -1




print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))



