# title: cinema-seat-allocation
# detail: https://leetcode.com/submissions/detail/385502037/
# datetime: Mon Aug 24 12:39:40 2020
# runtime: 672 ms
# memory: 17.7 MB

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_rows = collections.defaultdict(int)
        for i, j in reservedSeats:
            reserved_rows[i] |= 1 << j
        result = 0
        for k in reserved_rows.values():
            if (k >> 2) & 0x0f == 0:
                result += 1
                if (k >> 6) & 0x0f == 0:
                    result += 1
            elif (k >> 4) & 0x0f == 0:
                result += 1
            elif (k >> 6) & 0x0f == 0:
                result += 1
        return result + 2 * (n - len(reserved_rows))
            
            