"""
Example 1: 739. Daily Temperatures

Given an array of integers temperatures that represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith
  day to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.
"""

from typing import List

# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#
#     stack = []
#     ans = [0] * len(temperatures)
#
#
#     for i, temp in enumerate(temperatures):
#         while stack and temperatures[stack[-1]] <= temp:
#             lowertempindex = stack.pop()
#             ans[lowertempindex] = i - lowertempindex
#
#         stack.append(i)
#
#     return ans
#

def dailyTemperatures( temperatures: List[int]) -> List[int]:
    stack = []
    answer = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer
#
print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))