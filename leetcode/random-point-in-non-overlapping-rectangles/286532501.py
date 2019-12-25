# title: random-point-in-non-overlapping-rectangles
# detail: https://leetcode.com/submissions/detail/286532501/
# datetime: Tue Dec 17 11:43:33 2019
# runtime: 228 ms
# memory: 16.7 MB

import random
import bisect
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        a = 0
        for x1, y1, x2, y2 in self.rects:
            a += (x2 - x1 + 1) * (y2 - y1 + 1) 
            self.areas.append(a)
        self.total_area = a
        
    def pick(self) -> List[int]:
        area = random.randint(1, self.total_area)
        i = bisect.bisect_left(self.areas, area)
        x = random.randint(self.rects[i][0], self.rects[i][2])
        y = random.randint(self.rects[i][1], self.rects[i][3])
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# class Solution {
#     TreeMap<Integer, Integer> map;
#     int[][] arrays;
#     int sum;
#     Random rnd= new Random();
    
#     public Solution(int[][] rects) {
#         arrays = rects;
#         map = new TreeMap<>();
#         sum = 0;
        
#         for(int i = 0; i < rects.length; i++) {
#             int[] rect = rects[i];
						
#             // the right part means the number of points can be picked in this rectangle
#             sum += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
			
#             map.put(sum, i);
#         }
#     }
    
#     public int[] pick() {
#         // nextInt(sum) returns a num in [0, sum -1]. After added by 1, it becomes [1, sum]
#         int c = map.ceilingKey( rnd.nextInt(sum) + 1);
        
#         return pickInRect(arrays[map.get(c)]);
#     }
    
#     private int[] pickInRect(int[] rect) {
#         int left = rect[0], right = rect[2], bot = rect[1], top = rect[3];
        
#         return new int[]{left + rnd.nextInt(right - left + 1), bot + rnd.nextInt(top - bot + 1) };
#     }
# }