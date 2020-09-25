# title: number-of-burgers-with-no-waste-of-ingredients
# detail: https://leetcode.com/submissions/detail/393691663/
# datetime: Thu Sep 10 18:03:20 2020
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t = 4 * cheeseSlices - tomatoSlices
        if t >= 0 and t % 2 == 0:
            s = t // 2
            j = (tomatoSlices - 2 * s) // 4
            if j >= 0:
                return [j, s]
        return []