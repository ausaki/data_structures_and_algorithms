# title: find-the-winner-of-an-array-game
# detail: https://leetcode.com/submissions/detail/375986373/
# datetime: Tue Aug  4 23:18:33 2020
# runtime: 692 ms
# memory: 27.6 MB

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        current = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < current:
                counter[current] += 1
            else:
                current = arr[i]
                counter[current] = 1
            if counter[current] == k:
                return current            
        return current