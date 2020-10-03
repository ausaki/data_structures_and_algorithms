# title: subarrays-with-k-different-integers
# detail: https://leetcode.com/submissions/detail/401809049/
# datetime: Mon Sep 28 21:28:57 2020
# runtime: 388 ms
# memory: 16.9 MB

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        result = 0
        i, j = 0, 0
        cnt = collections.Counter()
        l = 0
        n = len(A)
        while j < n:
            cnt[A[j]] += 1
            j += 1
            if len(cnt) == K:
                l = 1
                while cnt[A[i]] > 1:
                    cnt[A[i]] -= 1
                    i += 1
                    l += 1
                result += l    
                break
        while j < n:
            if A[j] not in cnt:
                cnt.pop(A[i])
                i += 1
                l = 1
            cnt[A[j]] += 1
            while cnt[A[i]] > 1:
                cnt[A[i]] -= 1
                i += 1
                l += 1
            # print(j, l)
            result += l
            j += 1
        return result