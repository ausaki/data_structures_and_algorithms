# title: magical-string
# detail: https://leetcode.com/submissions/detail/286608581/
# datetime: Tue Dec 17 18:06:50 2019
# runtime: 108 ms
# memory: 27.3 MB

class Solution:
    magical_string = [[1, 1], [2,1 ], [2, 1]]
    index = 2
    def magicalString(self, n: int) -> int:
        i = self.index
        magical_string = self.magical_string
        while i < n:
            j = magical_string[i][0]
            k = 3 - magical_string[-1][0]
            magical_string.append([k, 0])
            if j == 2: magical_string.append([k, 0])
            if magical_string[i][0] == 1: 
                magical_string[i][1] = magical_string[i - 1][1] + 1
            else:
                magical_string[i][1] = magical_string[i - 1][1]
            i += 1
        self.__class__.index = i
        # print(magical_string)
        return magical_string[n - 1][1]