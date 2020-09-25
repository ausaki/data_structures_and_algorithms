# title: jump-game-iii
# detail: https://leetcode.com/submissions/detail/392311207/
# datetime: Mon Sep  7 22:24:19 2020
# runtime: 244 ms
# memory: 20.1 MB

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = collections.deque([start])
        while q:
            i = q.popleft()
            j = i + arr[i]
            for j in [i + arr[i], i - arr[i]]:
                if 0 <= j < n and arr[j] >= 0:
                    if arr[j] == 0:
                        return True
                    arr[j] = -arr[j]
                    q.append(j)
        return False
            
        