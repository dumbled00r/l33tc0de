"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.


Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
"""


def countElements(arr) -> int:
    ### O(N^2) solution / O(1) space complexity
    # cnt = 0
    # for num in arr:
    #     if num + 1 in arr:
    #         cnt += 1
    #
    # return cnt

    ### O(N) solution / O(1) space complexity
    setNums = set(arr)
    cnt = 0
    for num in arr:
        if num+1 in setNums:
            cnt+=1
    return cnt



print(countElements([1,2,3]))
