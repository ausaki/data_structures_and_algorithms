# title: html-entity-parser
# detail: https://leetcode.com/submissions/detail/384030407/
# datetime: Fri Aug 21 12:39:18 2020
# runtime: 132 ms
# memory: 14.8 MB

import re

class Solution:
    def entityParser(self, text: str) -> str:
        repl = {'&quot;': '"', '&apos;': "'", '&amp;': '&', '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        return re.sub(r'&(quot|apos|amp|gt|lt|frasl);', lambda m: repl[m.group(0)], text)