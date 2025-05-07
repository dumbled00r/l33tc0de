"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:

    dic = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        dic[s[right]] += 1
        while dic[s[right]] > 1: # appear more than once
            dic[s[left]] -= 1
            if dic[s[left]] == 0:
                del dic[s[left]]
            left += 1
        ans = max(ans, right - left + 1)

    return ans





print(lengthOfLongestSubstring("pwwkew"))


