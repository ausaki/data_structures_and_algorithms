# title: divide-array-in-sets-of-k-consecutive-numbers
# detail: https://leetcode.com/submissions/detail/392847815/
# datetime: Tue Sep  8 23:26:57 2020
# runtime: 616 ms
# memory: 36.2 MB

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = [[k, v] for k, v in collections.Counter(nums).items()]
        counter.sort(reverse=True)
        while len(counter) >= k:
            i = counter[-1][0]
            l = counter[-1][1]
            for j in range(k):
                if counter[-j - 1][0] == i + j:
                    counter[-j - 1][1] -= l
                    if j > 0 and counter[-j - 1][1] < counter[-j][1]:
                        return False
                else:
                    return False
            while counter and counter[-1][1] == 0:
                counter.pop()
        return True if len(counter) == 0 else False 
            