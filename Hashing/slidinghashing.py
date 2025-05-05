"""
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
"""
from collections import defaultdict


def find_longest_substring(s, k):
    dic = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        dic[s[right]] += 1
        while len(dic) > k:
            dic[s[left]] -= 1
            if dic[s[left]] == 0:
                del dic[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


print(find_longest_substring("eceba", 2))