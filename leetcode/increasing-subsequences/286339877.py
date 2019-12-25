# title: increasing-subsequences
# detail: https://leetcode.com/submissions/detail/286339877/
# datetime: Mon Dec 16 15:50:05 2019
# runtime: 220 ms
# memory: 23.5 MB

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seqs = {tuple(),}
        for num in nums:
            seqs |= {seq + (num, ) for seq in seqs if not seq or num >= seq[-1]}
        return [list(seq) for seq in seqs if len(seq) >= 2]
