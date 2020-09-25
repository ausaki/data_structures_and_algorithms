# title: rearrange-spaces-between-words
# detail: https://leetcode.com/submissions/detail/399143709/
# datetime: Tue Sep 22 17:43:27 2020
# runtime: 44 ms
# memory: 13.8 MB

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = re.findall(r'(\w+)', text)
        spaces = text.count(' ')
        s, r = divmod(spaces, len(words) - 1) if len(words) > 1 else (0, spaces)
        return (' ' * s).join(words) + ' ' * r
        