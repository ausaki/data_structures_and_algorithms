# def distance(a, b):
#     n, m = len(a), len(b)
    
#     dp = []
#     for i in range(n + 1):
#         if i == n:
#             row = [m - j for j in range(m + 1)]
#         else:
#             row = [n - i if j == m else 0 for j in range(m + 1)]
#         dp.append(row)

#     path = []
#     for i in range(n - 1, -1, -1):
#         for j in range(m - 1, -1, -1):
#             if a[i] == b[j]:
#                 dp[i][j] = dp[i + 1][j + 1]
#                 path.append()
#             else:
#                 dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])
#     # for row in dp:
#     #     print(row)

#     return dp[0][0]

class Myers:
    COL_DEL = '\033[31m'
    COL_INS = '\033[32m'
    COL_DEF = '\033[39m'

    def __init__(self, color_del=None, color_ins=None, color_default=None) -> None:
        self.color_del = color_del or self.COL_DEL
        self.color_ins = color_ins or self.COL_INS
        self.color_default = color_default or self.COL_DEF

    def diff(self, a, b):
        if len(a) == len(b) == 0:
            return ''
        trace = self._shortest_edit_distance(a, b)
        path = self._backtrack(a, b, trace)
        path = list(path)
        path.reverse()
        return self._gen_diff_output(a, b, path)

    def _shortest_edit_distance(self, a, b):
        n, m = len(a), len(b)
        nm = n + m
        # k 的最小值等于 -m, 最大值等于 n, 因此 v 的长度等于 n + m + 1
        v = [0] * (nm + 1)
        # 此时的 v 表示 d = -1 时状态, v[1] = 0 表示坐标 (0, -1)
        v[1] = 0
        trace = []
        for d in range(nm + 1):
            # 记录当前状态
            v = v[:]
            trace.append(v)
            # 计算 k 的最小最大值
            mink, maxk = -m + abs(m - d), n - abs(n - d)
            for k in range(mink, maxk + 1, 2):
                # 注意边界条件
                if d <= m and k == mink:
                    x = v[k + 1]
                elif d <= n and k == maxk:
                    x = v[k - 1] + 1
                elif v[k - 1] < v[k + 1]:
                    x = v[k + 1]
                else:
                    x = v[k - 1] + 1
                y = x - k
                while x < n and y < m and a[x] == b[y]:
                    x += 1
                    y += 1
                v[k] = x
                if x >= n and y >= m:
                    return trace
    
    def _backtrack(self, a, b, trace):
        n, m = len(a), len(b)
        x, y = n, m
        for d in reversed(range(len(trace))):
            v = trace[d]
            mink, maxk = -m + abs(m - d), n - abs(n - d)
            k = x - y
            if d <= m and k == mink:
                prev_k = k + 1
            elif d <= n and k == maxk:
                prev_k = k - 1
            elif v[k - 1] < v[k + 1]:
                prev_k = k + 1
            else:
                prev_k = k - 1
            prev_x, prev_y = v[prev_k], v[prev_k] - prev_k
            while x > prev_x and y > prev_y:
                yield (x - 1, y - 1, x, y)
                x -= 1
                y -= 1
            if d > 0:
                yield (prev_x, prev_y, x, y)
            x, y = prev_x, prev_y

    def _gen_diff_output(self, a, b, path):
        output = []
        temp = '{color}{action} {line}' + self.color_default
        for x0, y0, x1, y1 in path:
            if x1 == x0:
                output.append(temp.format(color=self.color_ins, action='+', line=b[y0]))
            elif y1 == y0:
                output.append(temp.format(color=self.color_del, action='-', line=a[x0]))
            else:
                output.append(temp.format(color=self.color_default, action=' ', line=a[x0]))
        return ''.join(output)



if __name__ == '__main__':
    import sys
    a, b = sys.argv[1], sys.argv[2]    
    fpa = open(a, 'r')
    fpb = open(b, 'r')
    print(Myers().diff(fpa.readlines(), fpb.readlines()))
    fpa.close()
    fpb.close()
