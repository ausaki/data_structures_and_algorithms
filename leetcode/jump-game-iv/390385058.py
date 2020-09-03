# title: jump-game-iv
# detail: https://leetcode.com/submissions/detail/390385058/
# datetime: Thu Sep  3 16:18:09 2020
# runtime: 536 ms
# memory: 28.4 MB

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = collections.defaultdict(list)
        for i, j in enumerate(arr):
            mp[j].append(i)
        visited = set()
        curr = {0}
        steps = 0
        while True:
            if n - 1 in curr:
                return steps
            new = set()
            for i in curr:
                if i > 0 and arr[i - 1] not in visited:
                    new.add(i - 1)
                if i < n - 1 and arr[i + 1] not in visited:
                    new.add(i + 1)
                if arr[i] in visited:
                    continue
                for j in mp[arr[i]]:
                    if j != i and j not in curr:
                        new.add(j)
                visited.add(arr[i])
            curr = new
            steps += 1
        return steps
        