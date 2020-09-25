# title: maximum-candies-you-can-get-from-boxes
# detail: https://leetcode.com/submissions/detail/392903143/
# datetime: Wed Sep  9 02:01:15 2020
# runtime: 860 ms
# memory: 26.5 MB

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = collections.deque(initialBoxes)
        closed = set()
        mycandies = 0
        while boxes:
            b = boxes.popleft()
            if status[b] == 0:
                closed.add(b)
                continue
            status[b] = -1
            mycandies += candies[b]
            for k in keys[b]:
                if k in closed:
                    boxes.append(k)
                    closed.remove(k)
                if status[k] == 0:
                    status[k] = 1
            for b_ in containedBoxes[b]:
                if status[b_] >= 0:
                    boxes.append(b_)
        return mycandies