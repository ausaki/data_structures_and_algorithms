# title: minimum-number-of-people-to-teach
# detail: https://leetcode.com/submissions/detail/446753130/
# datetime: Sat Jan 23 23:42:50 2021
# runtime: 1476 ms
# memory: 27.6 MB

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        g = set()
        # friendships = for a, b in friendships
        for a, b in friendships:
            a -= 1
            b -= 1
            if not (languages[a] & languages[b]):
                g.add(a)
                g.add(b)
        if not g:
            return 0
        cnt = collections.Counter()
        for a in g:
            for l in languages[a]:
                cnt[l] += 1
        return len(g) - cnt.most_common(1)[0][1]
        