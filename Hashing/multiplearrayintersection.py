"""
Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
"""
from collections import defaultdict


def intersection(nums):
    dic = defaultdict(int)
    for arr in nums:
        for _ in arr:
            dic[_] += 1
    ans = []
    for k in dic:
        if dic[k] == len(nums):
            ans.append(k)
    ans = sorted(ans)
    return ans

intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])

