# title: check-if-n-and-its-double-exist
# detail: https://leetcode.com/submissions/detail/387381557/
# datetime: Fri Aug 28 10:42:23 2020
# runtime: 52 ms
# memory: 13.9 MB

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = {arr[0]}
        for a in arr:
            if (a % 2 == 0 and a // 2 in s) or a * 2 in s:
                return True
            s.add(a)
        return False