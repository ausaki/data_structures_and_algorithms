# title: queue-reconstruction-by-height
# detail: https://leetcode.com/submissions/detail/285473485/
# datetime: Thu Dec 12 20:25:29 2019
# runtime: 104 ms
# memory: 13.3 MB

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N = len(people)
        res = []
        people.sort()
        i = N - 1
        while i >= 0:
            j = i - 1
            while j >= 0 and people[j][0] == people[j + 1][0]:
                j -= 1
            for k in range(j + 1, i + 1):
                cnt = people[k][1]
                res.insert(cnt, people[k])
            i = j
        return res