# title: number-of-burgers-with-no-waste-of-ingredients
# detail: https://leetcode.com/submissions/detail/393691073/
# datetime: Thu Sep 10 18:00:41 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        s, r = divmod(4 * cheeseSlices - tomatoSlices, 2)
        if s >= 0 and r == 0:
            j = (tomatoSlices - 2 * s) // 4
            if j >= 0:
                return [j, s]
        return []