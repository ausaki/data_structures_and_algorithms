# title: minimum-moves-to-move-a-box-to-their-target-location
# detail: https://leetcode.com/submissions/detail/394254234/
# datetime: Sat Sep 12 00:29:58 2020
# runtime: 44 ms
# memory: 14.1 MB



class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n, g = len(grid), len(grid[0]), collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[grid[i][j]] += [complex(i, j)]
        
        def f(b, s):
            nonlocal time
            time += 1
            boxToTarget = b - target
            return (abs((boxToTarget.real))+abs((boxToTarget).imag)+s, abs(boxToTarget), time)
        
        player, box, target, time = *g['S'], *g['B'], *g['T'], 1
        floor = {player, box, target, *g['.']}
        
        alpha = [(f(box, 1), 1, player, box)]
        directions, visited = (1, -1, 1j, -1j), set()   # 下上右左
        
        # 因为都不是数而是复数。因此采用字典映射的方式定义low dfn
        low = dict.fromkeys(floor, 0)  # 标准的dict.fromkeys创建字典。keys来源第一个参数第二个参数默认或赋值
        dfn = low.copy()
        count = 0
        index = {}
        # 标准无向图tarjan深度优先扩展函数，参数currIndex为当前拓展点，记录拓展的父节点防止重复拓展
        def tarjan(currIndex, parentIndex):
            nonlocal count
            count += 1
            dfn[currIndex] = low[currIndex] = count
            index[count] = currIndex
            for direction in directions:
                nextIndex = currIndex + direction
                if nextIndex in floor and nextIndex != parentIndex:
                    if not low[nextIndex]:
                        tarjan(nextIndex, currIndex)
                    low[currIndex] = min(low[currIndex], low[nextIndex])
        
        #运行tarjan函数，初始值为box的坐标，因为坐标都在复平面第一象限，初始父节点取-1不影响计算
        tarjan(box, -1)
        #print(low)
        #print(dfn)
        # 如果箱子在割点上仍可以移动的话，则箱子在移动的过程中，人的坐标也完成了强连通分量的转移，
        # 所以即便是宽度为1的碎片化的强连通分量隧道，也不影响上述结论。
        for currIndex in floor:  # 所有的可达点
            connect = [currIndex]
            while dfn[connect[-1]] != low[connect[-1]]:
                connect.append(index[low[connect[-1]]])
            for w in connect[:-2]:
                low[w] = low[connect[-1]]
        #print(low)
        
        # 计算完强连通分量后可以加一个剪枝，即如果人或目标点没被计算到，则表示三个关键点不在同一个并查集里面，
        # 可以直接返回-1
        if not low[player] * low[target]:
            return -1
        
        while alpha:
            _, steps, currPlayer, currBox = heapq.heappop(alpha)
            for direction in directions:
                nextPlayer, nextBox = currBox - direction, currBox + direction
                if nextBox in floor and nextPlayer in floor and (nextPlayer, currBox) not in visited and low[currPlayer] == low[nextPlayer]:
                    if nextBox == target:
                        return steps
                    heapq.heappush(alpha, (f(nextBox, steps + 1), steps + 1, currBox, nextBox))
                    visited.add((nextPlayer, currBox))
        return -1

