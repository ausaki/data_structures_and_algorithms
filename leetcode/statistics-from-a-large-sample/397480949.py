# title: statistics-from-a-large-sample
# detail: https://leetcode.com/submissions/detail/397480949/
# datetime: Fri Sep 18 22:24:39 2020
# runtime: 44 ms
# memory: 13.7 MB

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        result = [-1, 0, 0, -1, 0]
        n = 0
        for i, j in enumerate(count):
            if j == 0:
                continue
            if result[0] == -1:
                result[0] = i
            n += j
            result[1] = i
            result[2] += i * j
            if j > result[3]:
                result[3] = j
                result[4] = i
        result[2] /= n
        result[3] = -1
        m = 0
        for i, j in enumerate(count):
            m += j
            if m >= (n + 1)// 2:
                if result[3] == -1:
                    result[3] = i
                else:
                    result[3] = (result[3] + i) / 2
                if n % 2 :
                    break
                if m > (n + 1) // 2:
                    break
        return result