# title: find-the-duplicate-number
# detail: https://leetcode.com/submissions/detail/284555970/
# datetime: Sun Dec  8 22:19:10 2019
# runtime: 16 ms
# memory: 9.7 MB

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() > 1)
        {
            int slow = nums[0];
            int fast = nums[nums[0]];
            while (slow != fast)
            {
                slow = nums[slow];
                fast = nums[nums[fast]];
            }

            fast = 0;
            while (fast != slow)
            {
                fast = nums[fast];
                slow = nums[slow];
            }
            return slow;
        }
        return -1;
    }
};