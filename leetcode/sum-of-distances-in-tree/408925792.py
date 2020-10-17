# title: sum-of-distances-in-tree
# detail: https://leetcode.com/submissions/detail/408925792/
# datetime: Thu Oct 15 13:04:11 2020
# runtime: 392 ms
# memory: 25.8 MB

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
        
        def dfs(i, parent):
            children = g[i]
            cnt, dist = 1, 0
            for j, child in enumerate(children):
                if child == parent:
                    children[j] = None
                    continue
                cnt1, dist1 = dfs(child, i)
                children[j] = [child, cnt1, dist1 + cnt1]
                cnt += cnt1
                dist += dist1 + cnt1
            children.append([-1, cnt, dist])
            return cnt, dist
        
        def dfs2(i, p_cnt, p_dist):
            children = g[i]
            i_cnt, i_dist = children[-1][1], children[-1][2]
            result[i] = i_dist + p_dist + p_cnt
            for j, child in enumerate(children):
                if child is None or child[0] == -1:
                    continue
                c_cnt = p_cnt + i_cnt - child[1]
                c_dist = p_dist + p_cnt + i_dist - child[2]
                dfs2(child[0], c_cnt, c_dist)
            
        # root = 0 
        root = random.randint(0, N - 1)
        dfs(root, -1)
        result = [0] * N
        dfs2(root, 0, 0)
        return result