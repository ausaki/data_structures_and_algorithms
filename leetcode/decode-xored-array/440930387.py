# title: decode-xored-array
# detail: https://leetcode.com/submissions/detail/440930387/
# datetime: Sun Jan 10 10:33:28 2021
# runtime: 276 ms
# memory: 15.9 MB

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for e in encoded:
            res.append(res[-1] ^ e)
        return res