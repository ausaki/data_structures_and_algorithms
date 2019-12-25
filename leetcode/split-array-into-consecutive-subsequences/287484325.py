# title: split-array-into-consecutive-subsequences
# detail: https://leetcode.com/submissions/detail/287484325/
# datetime: Sat Dec 21 14:45:23 2019
# runtime: 592 ms
# memory: 14 MB

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        seqs = collections.Counter()
        orphans = collections.Counter(nums)
        for num in nums:
            if num not in orphans:
                continue
            orphans[num] -= 1
            if orphans[num] == 0:
                orphans.pop(num)
            if num - 1 in seqs:
                seqs[num - 1] -= 1
                if seqs[num - 1] == 0:
                    seqs.pop(num - 1)
                seqs[num] += 1
            elif num + 1 in orphans and num + 2 in orphans:
                orphans[num + 1] -= 1
                orphans[num + 2] -= 1
                if orphans[num + 1] == 0:
                    orphans.pop(num + 1)
                if orphans[num + 2] == 0:
                    orphans.pop(num + 2)
                seqs[num + 2] += 1
            else:
                return False
        return not orphans