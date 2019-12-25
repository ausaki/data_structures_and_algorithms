# title: utf-8-validation
# detail: https://leetcode.com/submissions/detail/279535173/
# datetime: Sun Nov 17 21:30:21 2019
# runtime: 112 ms
# memory: 12.9 MB

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        i = 0
        while i < N:
            byte = data[i]
            mask = 1 << 7
            count = 0
            while  count <= 4 and byte & mask > 0:
                count += 1
                mask = mask >> 1
            if count == 1 or count == 5:
                return False
            if count == 0:
                i += 1
                continue
            if i + count - 1 >= N:
                return False
            for j in range(1, count):
                if data[i + j] & 0xc0 != 0x80:
                    return False
            i += count
        return True
            