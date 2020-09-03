# title: parallel-courses-ii
# detail: https://leetcode.com/submissions/detail/380410115/
# datetime: Fri Aug 14 00:52:14 2020
# runtime: 9096 ms
# memory: 14.3 MB

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # from https://leetcode.com/problems/parallel-courses-ii/discuss/708445/Weak-test-case-most-solutions-posted-using-depth-or-outdgree-are-wrong
        preq = [0] * n
        for c1, c2 in dependencies:
            # to study j, what are the prerequisites?  each set bit is a class that we need to take. ith bit means ith class
            # minus 1 because classes are 1 to n
            preq[c2 - 1] |= 1 << (c1 - 1)
        dp = [n] * (1 << n)
        dp[0] = 0
        for i in range(1 << n):
            # we are now at status i. we can "influence" a later status from this status

            # what are the classes we can study?
            can_study = 0   
            for j in range(n):
                # a & b== b means b is a's subset
                # so if preq[j] is i's subset, we can now study j given status i
                if (i & preq[j]) == preq[j]:
                    can_study |= (1 << j)
            can_study &= ~i
            # take out i, so that we only enumerate a subset canStudy without i.
            # note we will | later so here we need a set that has no intersection with i to reduce the enumeration cost
            sub = can_study
            while sub > 0:
                # we can study one or more courses indicated by set "canStudy". we need to enumerate all non empty subset of it. 
				# This for loop is a typical way to enumerate all subsets of a given set "canStudy"
                # we studied i using dp[i] semesters. now if we also study the subset sub, we need dp [i ]+1 semesters, 
                # and the status we can "influence" is dp[ i | sub] because at that state, we studied what we want to study in "sub" 
                if bin(sub).count('1') <= k:
                    dp[i | sub] = min(dp[i | sub], dp[i] + 1)
                sub = (sub - 1) & can_study
        return dp[(1 << n) - 1]
                
        