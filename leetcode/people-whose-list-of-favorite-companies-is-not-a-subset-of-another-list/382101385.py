# title: people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
# detail: https://leetcode.com/submissions/detail/382101385/
# datetime: Mon Aug 17 14:42:52 2020
# runtime: 324 ms
# memory: 28.4 MB

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [(set(com), i) for i, com in enumerate(favoriteCompanies)]
        favoriteCompanies.sort(key=lambda a: len(a[0]))
        i = 0
        j = 1
        n = len(favoriteCompanies)
        result = []
        for i in range(n):
            while j < n and len(favoriteCompanies[i][0]) == len(favoriteCompanies[j][0]):
                j += 1
            for k in range(j, n):
                if favoriteCompanies[i][0].issubset(favoriteCompanies[k][0]):
                    break
            else:
                result.append(favoriteCompanies[i][1])
        result.sort()
        return result
                    
            
        
        