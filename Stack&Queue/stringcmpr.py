"""
Example 3: 844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".
"""


def backspaceCompare(s: str, t: str) -> bool:
    stackS = []
    stackT = []

    for _ in s:
        if _ == "#":
            stackS.pop()
        else:
            stackS.append(_)
    for _ in t:
        if _ == "#":
            stackT.pop()
        else:
            stackT.append(_)
    return stackS == stackT

print(backspaceCompare("ab#c","ad#c"))



