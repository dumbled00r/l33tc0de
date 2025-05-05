"""
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
"""
from collections import defaultdict


def areOccurrencesEqual(s: str) -> bool:
    dic = defaultdict(int)
    for _ in s:
        dic[_] += 1

    setOccurence = set(dic.values())
    return len(setOccurence) == 1

