# title: bulb-switcher
# detail: https://leetcode.com/submissions/detail/285019326/
# datetime: Tue Dec 10 20:54:15 2019
# runtime: 28 ms
# memory: 12.6 MB

import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))