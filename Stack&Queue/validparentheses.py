"""
Example 1: 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.

For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.
"""


def isValid(s: str) -> bool:
    stack = []
    dicParentheses = {
        "[": "]",
        "{": "}",
        "(": ")"
    }
    for p in s:
        if p in dicParentheses:
            stack.append(p)
        else:
            if not stack:
                return False
            if p != dicParentheses[stack.pop()]:
                return False
    # stack is empty --> true
    return not stack

print(isValid("["))