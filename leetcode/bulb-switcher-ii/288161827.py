# title: bulb-switcher-ii
# detail: https://leetcode.com/submissions/detail/288161827/
# datetime: Tue Dec 24 13:36:48 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def flipLights(self, n: int, m: int) -> int:
        n = min(n, 6)
        shift = max(0, 6 - n)
        seen = set()
        for op in range(16):
            cnt = bin(op)[2:].count('1')
            lights = 0;
            if cnt % 2 == m % 2 and cnt <= m:
                if (op >> 0) & 1:
                    lights ^= 0b111111 >> shift
                if (op >> 1) & 1:
                    lights ^= 0b010101 >> shift
                if (op >> 2) & 1:
                    lights ^= 0b101010 >> shift
                if (op >> 3) & 1:
                    lights ^= 0b100100 >> shift
                seen.add(lights)
        return len(seen)