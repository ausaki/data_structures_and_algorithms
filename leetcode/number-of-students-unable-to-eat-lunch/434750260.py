# title: number-of-students-unable-to-eat-lunch
# detail: https://leetcode.com/submissions/detail/434750260/
# datetime: Sat Dec 26 22:37:43 2020
# runtime: 64 ms
# memory: 14.2 MB

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = collections.Counter(students)
        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
            else:
                break
        return sum(cnt.values()) 
        
            