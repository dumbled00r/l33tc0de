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
    converted_arr = []
    for _ in nums:
        if _ == 1:
            converted_arr.append(1)
        else: converted_arr.append(-1)
    print(converted_arr)

    # find number of sub arrays that sum up  to 0 (meaning that # 0s = # 1s)
    dic = defaultdict(int)
    dic[0] = 1 # base case, empty array --> prefix = 0
    curr = 0
    k = 0

    ans = 0
    max_len = 0
    for i, num in enumerate(converted_arr):
        curr += num
        if curr-k in dic:
            ans += dic[curr-k]
            max_len = max(max_len, i - dic[curr-k])
        dic[curr] +=1

    print(ans) # 4 sub arrays that # 0s = # 1s
    print(max_len)



print(findMaxLength([0,1]))

