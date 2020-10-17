# title: boats-to-save-people
# detail: https://leetcode.com/submissions/detail/406167200/
# datetime: Thu Oct  8 22:37:17 2020
# runtime: 496 ms
# memory: 21.1 MB

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i = 0
        j = n
        result = 0
        while i < j:
            k = bisect.bisect(people, limit - people[i], i + 1, j)
            if k == i + 1:
                result += j - i
                break
            result += 1 + j - k
            i += 1
            j = k - 1
        return result