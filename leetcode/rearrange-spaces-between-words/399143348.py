# title: rearrange-spaces-between-words
# detail: https://leetcode.com/submissions/detail/399143348/
# datetime: Tue Sep 22 17:41:58 2020
# runtime: 28 ms
# memory: 13.8 MB

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = re.findall(r'(\w+)', text)
        spaces = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * spaces
        s, r = divmod(spaces, len(words) - 1)
        return (' ' * s).join(words) + ' ' * r
        