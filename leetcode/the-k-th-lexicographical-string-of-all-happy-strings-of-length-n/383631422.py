# title: the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
# detail: https://leetcode.com/submissions/detail/383631422/
# datetime: Thu Aug 20 16:21:35 2020
# runtime: 132 ms
# memory: 18.6 MB

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 3 * (2 ^ (n - 1))
        all_strs = []
        def gen(prev):
            if len(prev) == n:
                all_strs.append(prev)
                return
            for c in ['a', 'b', 'c']:
                if prev and c == prev[-1]:
                    continue
                gen(prev + c)
        N = 3 * (1 << (n - 1))
        if k > N:
            return ''
        gen('')
        # print(all_strs)
        return all_strs[k - 1]