"""
Example 2: 1047. Remove All Adjacent Duplicates In String

You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.

For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.

"""

def removeDuplicate(s: str) -> str:
    stack = []
    for _ in s:
        if stack and stack[-1] == _:
            stack.pop()
        else:
            stack.append(_)

    return "".join(stack)

print(removeDuplicate("aababaab"))
