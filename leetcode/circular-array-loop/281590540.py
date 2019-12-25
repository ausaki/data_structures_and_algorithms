# title: circular-array-loop
# detail: https://leetcode.com/submissions/detail/281590540/
# datetime: Mon Nov 25 23:59:34 2019
# runtime: 52 ms
# memory: 12.9 MB

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 0:
            return False
        i = 0
        visited = set()
        path = {}
        direction = nums[i]
        step = 0
        while True:
            if step == 0:
                if i in visited:
                    j = (i + 1) % N
                    while j != i and j in visited:
                        j = (j + 1) % N
                    if j == i:
                        break
                    i = j
                direction = nums[i]
                visited.add(i)
                path = {i: 0}
                step = 1
                # print('start', i, direction)
                i = (i + nums[i]) % N
                continue
            # print('traverse', i)
            if i in visited:
                if i in path and step - path.get(i) > 1:
                    return True
                step = 0
                continue
            if (direction ^ nums[i]) >= 0:
                visited.add(i)
                path[i] = step
                i = (i + nums[i]) % N
                step += 1
                
            else:
                step = 0
        return False