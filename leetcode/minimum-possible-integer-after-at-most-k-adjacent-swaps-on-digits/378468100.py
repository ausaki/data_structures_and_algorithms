# title: minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits
# detail: https://leetcode.com/submissions/detail/378468100/
# datetime: Mon Aug 10 01:25:46 2020
# runtime: 308 ms
# memory: 15.5 MB

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n * (n - 1) / 2:
            return ''.join(sorted(num))
        digits_indices = collections.defaultdict(collections.deque)
        for i, d in enumerate(num):
            digits_indices[d].append(i)
        removed_indices = []
        result = []
        while k and len(result) < n:
            for d in '0123456789':
                if d not in digits_indices or len(digits_indices[d]) == 0:
                    continue
                idx = digits_indices[d][0]
                i = bisect.bisect(removed_indices, idx)
                if k >= idx - i:
                    k -= idx - i
                    removed_indices.insert(i, idx)
                    digits_indices[d].popleft()
                    result.append(d)
                    break
        if len(result) < n:
            j = 0
            for i, d in enumerate(num):
                if j >= len(removed_indices) or i < removed_indices[j]:
                    result.append(d)
                else:
                    j += 1
        return ''.join(result)
