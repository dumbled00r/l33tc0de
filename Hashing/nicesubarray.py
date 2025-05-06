"""
Example 5: 1248. Count Number of Nice Subarrays

Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2. The subarrays with 3 odd numbers in them are [1, 1, 2, 1] and [1, 2, 1, 1].

"""
from collections import defaultdict


def numberOfSubarrays(nums, k: int) -> int:
    dic = defaultdict(int)
    dic[0] = 1
    ans = 0
    curr = 0
    for num in nums:
        if num % 2 != 0:
            curr += 1
            ans += dic[curr-k]
            dic[curr] += 1

    return ans

print(numberOfSubarrays([1, 1, 2, 1, 1], 3))
