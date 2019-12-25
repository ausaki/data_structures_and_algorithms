# title: increasing-subsequences
# detail: https://leetcode.com/submissions/detail/286338584/
# datetime: Mon Dec 16 15:42:58 2019
# runtime: 224 ms
# memory: 22.7 MB

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seqs = set()
        for num in nums:
            tmp = set()
            for seq in seqs:
                if num >= seq[-1]:
                    new_seq = list(seq)
                    new_seq.append(num)
                    tmp.add(tuple(new_seq))
            seqs |= tmp
            seqs.add((num,))
        res = []
        for seq in seqs:
            if len(seq) >= 2:
                res.append(list(seq))
        return res