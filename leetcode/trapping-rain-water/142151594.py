# title: trapping-rain-water
# detail: https://leetcode.com/submissions/detail/142151594/
# datetime: Sat Feb 24 18:46:55 2018
# runtime: 77 ms
# memory: N/A

class Solution(object):
    def _trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        water_units = 0
        i = 0
        left = -1
        right = -1
        while i < length - 1:
            if height[i] <= height[i + 1]:
                i += 1
                continue
            # 
            block_units = height[i + 1]
            left = i
            i += 2
            while i < length and height[i] < height[left + 1]:
                block_units += height[i]
                i += 1
            right = i
            # 计算 left 和 right 之间的水量
            if right >= length:
                right = length - 1
                block_units -= height[right]
            min_height = min(height[left], height[right])
            water_units += min_height * (right - left - 1) - block_units
        return water_units
    
    def strip(self, height):
        """清理左右两边的 0
        """
        length = len(height)
        i = 0
        j = length - 1

        while i < j and (height[i] == 0 or height[j] == 0):
            if height[i] == 0:
                i += 1
            if height[j] == 0:
                j -= 1
        if i >= j:
            return []
        return height[i: j + 1]
        
        
    def trap(self, height):
        if not height:
            return 0

        height = self.strip(height)
        
        if not height:
            return 0
        
        length = len(height)
        water_units = 0
        i = 0
        j = length - 1
        
        # print 'i: {0}, j: {1}'.format(i, j)
        
        while i < j:
            min_height = 0
            min_index_left = True
            if height[i] > height[j]:
                min_height = height[j]
                min_index_left = False
            else:
                min_height = height[i]
                min_index_left = True
            
            # print 'i: {0}, j: {1}'.format(i, j)
            # print 'min_height: {0}, min_index_left: {1}'.format(min_height, min_index_left)
            
            l = i + 1
            r = j - 1
            moved = False
            while l <= r:
                if height[l] < min_height:
                    w = min_height - height[l]
                    water_units += w
                    height[l] = min_height
                    # print '+l water[{0}]: {1}'.format(l, w)
                    
                elif not moved and min_index_left:
                    i = l
                    moved = True
                if l != r and height[r] < min_height :
                    w = min_height - height[r]
                    water_units += w
                    height[r] = min_height
                    # print '+r water[{0}]: {1}'.format(r, w)
                    
                elif height[r] > min_height and not moved and not min_index_left:
                    j = r
                    moved = True
                l += 1
                r -= 1
            
            if not moved:
                # print 'not moved'
                if min_index_left:
                    # print 'left'
                    while l < j and height[l] <= min_height:
                        l += 1
                    if l < j:
                        moved = True
                        i = l
                else:
                    # print 'right'
                    # print 'r: {0}'.format(r)
                    while r > i and height[r] <= min_height:
                        r -= 1
                    if r > i:
                        moved = True
                        j = r
            if not moved:
                break
                
        return water_units
            
            
        
            