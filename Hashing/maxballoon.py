"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:



Input: text = "nlaebolko"
Output: 1
"""
from collections import defaultdict


def maxNumberOfBalloons(text: str) -> int:
    # dic = defaultdict(int)
    # ans = 0
    # for char in text:
    #     dic[char] = dic.get(char, 0) + 1
    #
    # while True:
    #     for char in 'balloon':
    #         if dic.get(char, 0) > 0:
    #             dic[char] -= 1
    #             canUse = True
    #         else:
    #             canUse = False
    #             break
    #     if canUse:
    #         ans += 1
    #     else: break
    # return ans

    dic = defaultdict(int)
    for char in "balloon":
        dic[char] = 0
    seenl = 0
    seeno = 0
    for char in text:
        if char in "balloon":
            if char == "l":
                seenl += 1
                if seenl == 2:
                    dic[char] += 1
                    seenl = 0
            elif char == 'o':
                seeno += 1
                if seeno == 2:
                    dic[char] += 1
                    seeno = 0
            else:
                dic[char] += 1
    return min(dic.values())

print(maxNumberOfBalloons("nlaebolko"))
