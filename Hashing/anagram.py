"""
Example 1: 49. Group Anagrams

Given an array of strings strs, group the anagrams together.

For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
"""
from collections import defaultdict


def groupAnagrams(strs):
    dic = defaultdict(list)
    for _ in strs:
        fullword = "".join(sorted(_))
        dic[fullword].append(_)
    return list(dic.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))