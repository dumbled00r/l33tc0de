"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

"""
from collections import defaultdict

def findMaxLength(nums):
    prefix = defaultdict(int)
    prefix[0] = -1 # the first index where prefix = 0 is -1 (empty array)

    currSum = 0 # tracking prefix sum
    k = 0
    maxlen = 0
    for i, num in enumerate(nums):
        if num == 1:
            currSum += 1
        else: currSum -= 1

        if currSum-k in prefix:
            maxlen = max(maxlen, i - prefix[currSum-k])
        else:
            prefix[currSum-k] = i

    return maxlen




print(findMaxLength([0,1,1,1,1,1,0,0,0]))

