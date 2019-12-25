# title: bulb-switcher
# detail: https://leetcode.com/submissions/detail/285019294/
# datetime: Tue Dec 10 20:53:58 2019
# runtime: 36 ms
# memory: 12.9 MB

import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))