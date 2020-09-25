# title: decompress-run-length-encoded-list
# detail: https://leetcode.com/submissions/detail/391858449/
# datetime: Sun Sep  6 23:01:10 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        val, freq = 0,1
        while (val < len(nums)):
            if val % 2 == 0:
                freq = nums[val]
            else:
                x = (str(nums[val]) + ',') * freq
                res.append(x[:-1])
            val += 1
        print(res)
        return res
