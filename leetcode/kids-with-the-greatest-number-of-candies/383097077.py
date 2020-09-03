# title: kids-with-the-greatest-number-of-candies
# detail: https://leetcode.com/submissions/detail/383097077/
# datetime: Wed Aug 19 14:53:18 2020
# runtime: 40 ms
# memory: 13.9 MB

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [c + extraCandies >= m for c in candies]