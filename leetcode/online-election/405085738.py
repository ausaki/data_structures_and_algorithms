# title: online-election
# detail: https://leetcode.com/submissions/detail/405085738/
# datetime: Tue Oct  6 11:20:35 2020
# runtime: 588 ms
# memory: 19 MB

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        cnt = collections.Counter()
        m = -1
        for i, p in enumerate(persons):
            cnt[p] += 1
            if cnt[p] >= cnt[m]:
                m = p
            persons[i] = m
        self.persons = persons
        self.times = times
    def q(self, t: int) -> int:
        i = bisect.bisect(self.times, t)
        return self.persons[i - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)