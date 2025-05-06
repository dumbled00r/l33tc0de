"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

"""
from collections import defaultdict


def findWinners(matches):
    ans = [[], []]

    winTimes = defaultdict(int)
    loseTimes = defaultdict(int)
    for match in matches:
        winTimes[match[0]] += 1
        loseTimes[match[1]] += 1
    for winner in winTimes:
        if winner not in loseTimes:
            ans[0].append(winner)
    for loser in loseTimes:
        if loseTimes[loser] == 1:
            ans[1].append(loser)
    ans[0] = sorted(ans[0])
    ans[1] = sorted(ans[1])

    return ans
print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
