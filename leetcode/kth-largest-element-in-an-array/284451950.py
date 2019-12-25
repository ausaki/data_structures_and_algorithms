# title: kth-largest-element-in-an-array
# detail: https://leetcode.com/submissions/detail/284451950/
# datetime: Sun Dec  8 11:05:45 2019
# runtime: 76 ms
# memory: 13.8 MB


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def _bysort():
            return sorted(nums, reverse=True)[k - 1]
        
        def _byheap():
            import heapq
            h = nums[:k]
            heapq.heapify(h)
            for i in range(k, len(nums)):
                if nums[k] < h[0]:
                    continue
                heapq.heapreplace(h, nums[k])
            return h[0]
        
        def _quickselect(k, left, right):
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                nums[left], nums[mid] = nums[mid], nums[left]
            if nums[mid] > nums[right]:
                nums[mid], nums[right] = nums[right], nums[mid]
            if nums[left] > nums[mid]:
                nums[left], nums[mid] = nums[mid], nums[left]
            if right - left + 1 <= 3:
                return nums[k]
            print(nums)
            pivot = nums[mid]
            nums[mid], nums[right - 1] = nums[right - 1], nums[mid]
            i = left + 1
            j = right - 2
            while True:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                else:
                    break
            nums[i], nums[right - 1] = nums[right - 1], nums[i]
            if i == k:
                return nums[i]
            elif i < k:
                return _quickselect(k, i + 1, right)
            else:
                return _quickselect(k, left, i - 1)
                
            
        return _quickselect(len(nums) - k, 0, len(nums) - 1)
            