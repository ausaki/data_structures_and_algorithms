# title: find-a-value-of-a-mysterious-function-closest-to-target
# detail: https://leetcode.com/submissions/detail/377750258/
# datetime: Sat Aug  8 14:38:21 2020
# runtime: 1072 ms
# memory: 79.4 MB

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        MAX_ABS = target + 10 ** 7
        N = len(arr)
        new_arr = [arr[0]]
        for i in range(1, N):
            if arr[i] == new_arr[-1]:
                continue
            new_arr.append(arr[i])
        arr = new_arr
        N = len(arr)
        result = MAX_ABS
        @lru_cache(None)
        def find(j, prev):
            if j >= N:
                return abs(prev - target)
            curr = arr[j] & prev
            if curr == target:
                return 0
            if curr < target:
                return min(abs(prev - target), abs(curr - target))
            return find(j + 1, curr)
        
        for i in range(N):
            if arr[i] == target:
                result = 0
                break
            if arr[i] < target:
                result = min(result, abs(arr[i] - target))
                continue
            m = find(i + 1, arr[i])
            result = min(result, m)
        return result
        
                
                    