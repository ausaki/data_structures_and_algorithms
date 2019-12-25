# title: swap-adjacent-in-lr-string
# detail: https://leetcode.com/submissions/detail/283684925/
# datetime: Wed Dec  4 22:19:26 2019
# runtime: 52 ms
# memory: 13.5 MB

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # S = len(start)
        # E = len(end)
        # if S != E:
        #     return False
        # i = 0
        # start = list(start)
        # end = list(end)
        # while i < S:
        #     if start[i] == end[i]:
        #         i += 1
        #     else:
        #         if start[i] == 'X' and end[i] == 'L':
        #             k = i + 1
        #             while k < S and start[k] == 'X':
        #                 k += 1
        #             if k < S and start[k] == 'L':
        #                 start[i], start[k] = start[k], start[i]
        #                 i += 1
        #             else:
        #                 return False
        #         elif start[i] == 'R' and end[i] == 'X':
        #             k = i + 1
        #             while k < S and start[k] == 'R':
        #                 k += 1
        #             if k < S and start[k] == 'X':
        #                 start[i], start[k] = start[k], start[i]
        #                 i += 1
        #             else:
        #                 return False
        #         else:
        #             return False
        # return True
        
        # 参考discuss
        if len(start) != len(end):
            return False
        sindex = [[i, ch] for i, ch in enumerate(start) if ch in 'LR']
        eindex = [[i, ch] for i, ch in enumerate(end) if ch in 'LR']
        if len(sindex) != len(eindex):
            return False
        for i in range(len(sindex)):
            j, ch1 = sindex[i]
            k, ch2 = eindex[i]
            if ch1 != ch2:
                return False
            if ch1 == 'L':
                if k > j:
                    return False
            else:
                if j > k:
                    return False
        return True