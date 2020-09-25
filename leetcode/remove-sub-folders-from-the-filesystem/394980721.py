# title: remove-sub-folders-from-the-filesystem
# detail: https://leetcode.com/submissions/detail/394980721/
# datetime: Sun Sep 13 14:56:02 2020
# runtime: 256 ms
# memory: 29.7 MB

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        fs = set(folder)
        for f in folder:
            i = 1
            while i < len(f):
                i = f.find('/', i)
                if i == -1:
                    break 
                if f[:i] in fs:
                    fs.remove(f)
                    break
                i += 1
        return list(fs)                