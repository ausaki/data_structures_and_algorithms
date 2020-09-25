# title: distribute-candies-to-people
# detail: https://leetcode.com/submissions/detail/397378239/
# datetime: Fri Sep 18 15:18:21 2020
# runtime: 36 ms
# memory: 14.1 MB

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        s = 1
        i = 1
        result = [0] * num_people
        while s <= candies:
            result[(i - 1) % num_people] += i
            i += 1
            s += i
        if s - i < candies:
            result[(i - 1) % num_people] += candies - (s - i)
        return result
            