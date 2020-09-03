# title: find-the-winner-of-an-array-game
# detail: https://leetcode.com/submissions/detail/375987117/
# datetime: Tue Aug  4 23:20:12 2020
# runtime: 876 ms
# memory: 27.5 MB

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] < current:
                count += 1
            else:
                current = arr[i]
                count = 1
            if count == k:
                return current
        return current