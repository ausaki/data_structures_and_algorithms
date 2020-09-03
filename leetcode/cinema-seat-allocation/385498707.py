# title: cinema-seat-allocation
# detail: https://leetcode.com/submissions/detail/385498707/
# datetime: Mon Aug 24 12:30:00 2020
# runtime: 1168 ms
# memory: 17.7 MB

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_rows = collections.defaultdict(int)
        for i, j in reservedSeats:
            reserved_rows[i] |= 1 << j
        rows = sorted(reserved_rows)
        result = 0
        for i, j in enumerate(rows):
            k = reserved_rows[j]
            if (k >> 2) & 0x0f == 0:
                result += 1
                if (k >> 6) & 0x0f == 0:
                    result += 1
            elif (k >> 4) & 0x0f == 0:
                result += 1
            elif (k >> 6) & 0x0f == 0:
                result += 1
            result += 2 * (rows[i] -  1 - (rows[i - 1] if i > 0 else 0))
        return result + 2 * (n - rows[-1])
            
            