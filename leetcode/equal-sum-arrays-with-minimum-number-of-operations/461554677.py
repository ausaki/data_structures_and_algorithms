# title: equal-sum-arrays-with-minimum-number-of-operations
# detail: https://leetcode.com/submissions/detail/461554677/
# datetime: Sun Feb 28 12:18:59 2021
# runtime: 4008 ms
# memory: 18.5 MB

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2: return 0
        if n > 6 * m or m > 6 * n: return -1
            
        g1, g2 = collections.Counter(nums1), collections.Counter(nums2)
        # if s1 > s2:
        #     s1, s2 = s2, s1
        #     g1, g2 = g2, g1
        #     n, m = m, n
        
        def calc(target, s, g):
            if s == target:
                return 0
            if s < target:
                cnt = 0
                target -= s
                for i in range(1, 6):
                    k = g[i]
                    q, r = divmod(target, (6 - i))
                    q += r != 0
                    if q > k:
                        cnt += k
                        target -= k * (6 - i)
                    else:
                        cnt += q
                        target = 0
                        break
                return cnt if target == 0 else -1
            cnt = 0
            target = s - target
            for i in range(6, 1, -1):
                k = g[i]
                q, r = divmod(target, (i - 1))
                q += r != 0
                if q > k:
                    cnt += k
                    target -= k * (i - 1)
                else:
                    cnt += q
                    target = 0
            return cnt if target == 0 else -1
        
        
        res = math.inf
        for s in range(max(n, m), 6 * min(n, m) + 1):
            i = calc(s, s1, g1)
            if i == -1:
                continue
            j = calc(s, s2, g2)
            if j == -1:
                continue
            # print(s, i, j)
            res = min(res, i + j)
        return res
            