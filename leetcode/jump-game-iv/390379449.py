# title: jump-game-iv
# detail: https://leetcode.com/submissions/detail/390379449/
# datetime: Thu Sep  3 16:00:05 2020
# runtime: 576 ms
# memory: 33.1 MB

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = collections.defaultdict(list)
        for i, j in enumerate(arr):
            mp[j].append(i)
        visited = set()
        visited1 = set()
        curr = {0}
        steps = 0
        while True:
            if n - 1 in curr:
                return steps
            new = set()
            for i in curr:
                if i > 0 and (i - 1 not in visited) :
                    new.add(i - 1)
                if i < n - 1 and (i + 1 not in visited):
                    new.add(i + 1)
                if arr[i] in visited1:
                    continue
                for j in mp[arr[i]]:
                    if (j not in visited) and (j not in curr):
                        new.add(j)
                visited1.add(arr[i])
            visited.update(curr)
            curr = new
            steps += 1
        return steps
        