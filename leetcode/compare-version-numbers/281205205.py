# title: compare-version-numbers
# detail: https://leetcode.com/submissions/detail/281205205/
# datetime: Sun Nov 24 11:16:29 2019
# runtime: 20 ms
# memory: 12.7 MB

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        N1 = len(version1)
        N2 = len(version2)
        i = 0
        j = 0
        while i < N1 or j < N2:
            v1 = 0
            v2 = 0
            while i < N1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < N2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            i += 1
            j += 1
        return 0
        