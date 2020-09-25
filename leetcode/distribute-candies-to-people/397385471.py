# title: distribute-candies-to-people
# detail: https://leetcode.com/submissions/detail/397385471/
# datetime: Fri Sep 18 15:40:46 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = int((math.sqrt(1 + 8 * candies) - 1) // 2)
        rem = candies - n * (1 + n) // 2
        i, j = divmod(n - 1, num_people)
        result = [0] * num_people
        for k in range(num_people):
            if k <= j:
                result[k] = (i + 1) * (k + 1 + k + 1 + num_people * i) // 2
            else:
                result[k] = i * (k + 1 + k + 1 + num_people * (i - 1)) // 2
        if rem:
            result[(j + 1) % num_people] += rem
        return result