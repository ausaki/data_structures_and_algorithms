# title: form-array-by-concatenating-subarrays-of-another-array
# detail: https://leetcode.com/submissions/detail/458377159/
# datetime: Sat Feb 20 22:55:59 2021
# runtime: 108 ms
# memory: 14.7 MB

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        def partial_table(sub):
            m = len(sub)
            table = [0] * (m + 1)
            table[0] = -1
            i = 0
            while i < m:
                j = table[i]
                while j >= 0 and sub[i] != sub[j]:
                    j = table[j]
                i += 1
                table[i] = j + 1
            return table


        def search_sub_kmp(s, sub):
            n = len(s)
            m = len(sub)
            if n == 0:
                if m == 0:
                    return 0
                else:
                    return -1
            elif m == 0:
                return 0

            table = partial_table(sub)
            i = 0
            j = 0
            while i < n:
                if s[i] == sub[j]:
                    i += 1
                    j += 1
                    if j == m:
                        # find
                        break
                else:
                    j = table[j]
                    if j < 0:
                        j = 0
                        i += 1
            if j == m:
                return i - j
            return -1
        
        for g in groups:
            m = len(g)
            i = search_sub_kmp(nums, g)
            if i == -1:
                return False
            i += m
            nums = nums[i:]
        return True