# title: avoid-flood-in-the-city
# detail: https://leetcode.com/submissions/detail/380283857/
# datetime: Thu Aug 13 17:44:50 2020
# runtime: 1240 ms
# memory: 31.1 MB

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        result = [1] * n
        lakes = {}
        days_no_rain = []
        for i, lake in enumerate(rains):
            if lake == 0:
                days_no_rain.append(i)
                continue
            result[i] = -1
            if lake not in lakes:
                lakes[lake] = i
                continue
            day = lakes[lake]
            j = bisect.bisect(days_no_rain, day)
            if j >= len(days_no_rain):
                return []
            k = days_no_rain.pop(j)
            result[k] = lake
            lakes[lake] = i
        # for day in days_no_rain:
        #     result[day] = 1
        return result
        