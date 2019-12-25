# title: h-index-ii
# detail: https://leetcode.com/submissions/detail/284720666/
# datetime: Mon Dec  9 13:10:43 2019
# runtime: 152 ms
# memory: 19.4 MB

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        if N == 0:
            return 0
        i = 0
        j = N - 1
        while i <= j:
            mid = (i + j) // 2
            print(mid, citations[mid], N - mid)
            if citations[mid] > N - mid:
                j = mid - 1
            elif citations[mid] < N - mid:
                i = mid + 1
            else:
                return citations[mid]
        print(j)
        return max(citations[j], N - j - 1) if j >= 0 else N
                