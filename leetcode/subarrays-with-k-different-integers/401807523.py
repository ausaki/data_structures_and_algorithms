# title: subarrays-with-k-different-integers
# detail: https://leetcode.com/submissions/detail/401807523/
# datetime: Mon Sep 28 21:23:02 2020
# runtime: 416 ms
# memory: 16.8 MB

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        result = 0
        i, j = 0, 0
        cnt = collections.Counter()
        l = 0
        n = len(A)
        while j < n:
            if len(cnt) != K:
                cnt[A[j]] += 1
                if len(cnt) == K:
                    l = 1
                    while cnt[A[i]] > 1:
                        cnt[A[i]] -= 1
                        i += 1
                        l += 1
                    result += l    
                    # print(j ,l)
            else:
                if A[j] in cnt:
                    cnt[A[j]] += 1
                    while cnt[A[i]] > 1:
                        cnt[A[i]] -= 1
                        i += 1
                        l += 1
                    # print(j, l)
                    result += l                        
                else:
                    cnt[A[i]] -= 1
                    if cnt[A[i]] == 0:
                        cnt.pop(A[i])
                    cnt[A[j]] += 1
                    i += 1
                    l = 1
                    while cnt[A[i]] > 1:
                        cnt[A[i]] -= 1
                        i += 1
                        l += 1
                    # print(j, l)
                    result += l
            j += 1
        return result