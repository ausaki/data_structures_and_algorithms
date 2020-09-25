# title: remove-sub-folders-from-the-filesystem
# detail: https://leetcode.com/submissions/detail/394984364/
# datetime: Sun Sep 13 15:06:22 2020
# runtime: 220 ms
# memory: 27.9 MB

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(reverse=True)
        result = []
        prefix = folder.pop()
        result.append(prefix)
        while folder:
            f = folder.pop()
            if not (f.startswith(prefix) and f[len(prefix)] == '/'):
                prefix = f
                result.append(prefix)
        return result
