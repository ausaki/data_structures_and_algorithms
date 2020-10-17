# title: similar-string-groups
# detail: https://leetcode.com/submissions/detail/408663610/
# datetime: Wed Oct 14 22:58:11 2020
# runtime: 556 ms
# memory: 15.4 MB



class Solution:
    def similar(self, x, y):
        cnt = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
            if cnt > 2:
                return False
        return True 

    def numSimilarGroups(self, A: List[str]) -> int:
        wordlen = len(A[0])
        A=set(A)
        divs = defaultdict(list)
        if wordlen > 6:
            for word in A:
                step = wordlen // 3
                for i in range(0, step * 3, step):
                    divs[word[i:i+step] + str(i)].append(word)
        else:
            divs['all'].extend(A)
        
        graph = defaultdict(set)
        for _list in divs.values():
            for i, a in enumerate(_list):
                for j, b in enumerate(_list[i+1:], i+1):
                    if self.similar(a, b):
                        graph[a].add(b)
                        graph[b].add(a)
        
        ans = 0 
        cc = set()
        for word in A:
            if word not in cc:
                queue = [word]
                while queue:
                    cur = queue.pop()
                    cc.add(cur)
                    for nx in graph[cur]:
                        if nx not in cc:
                            queue.append(nx)
                ans += 1
        return ans 
        

