# title: jump-game-iv
# detail: https://leetcode.com/submissions/detail/390388114/
# datetime: Thu Sep  3 16:28:06 2020
# runtime: 576 ms
# memory: 28.3 MB

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = collections.defaultdict(list)
        for i, j in enumerate(arr):
            mp[j].append(i)
        visited = set()
        curr = collections.deque([0])
        steps = 0
        while True:
            for _ in range(len(curr)):
                i = curr.popleft()
                if i == n - 1:
                    return steps
                if i > 0 and arr[i - 1] not in visited:
                    curr.append(i - 1)
                if i < n - 1 and arr[i + 1] not in visited:
                    curr.append(i + 1)
                if arr[i] in visited:
                    continue
                for j in mp[arr[i]]:
                    if j != i:
                        curr.append(j)
                visited.add(arr[i])
            steps += 1
        return steps
        