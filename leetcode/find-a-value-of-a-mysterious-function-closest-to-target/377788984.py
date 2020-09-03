# title: find-a-value-of-a-mysterious-function-closest-to-target
# detail: https://leetcode.com/submissions/detail/377788984/
# datetime: Sat Aug  8 16:41:40 2020
# runtime: 3344 ms
# memory: 28.5 MB

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
        for i in range(N):
            if arr[i] == target:
                result = 0
                break
            if arr[i] < target:
                result = min(result, abs(arr[i] - target))
                continue
            prev = arr[i]
            for j in range(i + 1, N):
                curr = arr[j] & prev
                if curr == target:
                    return 0
                if curr < target:
                    result = min(result, abs(prev - target), abs(curr - target))
                    break
                prev = curr
            result = min(result, abs(prev - target))
        return result
        
                
                    