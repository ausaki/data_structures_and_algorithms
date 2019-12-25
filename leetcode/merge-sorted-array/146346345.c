// title: merge-sorted-array
// detail: https://leetcode.com/submissions/detail/146346345/
// datetime: Thu Mar 22 11:39:54 2018
// runtime: 4 ms
// memory: N/A

void merge(int* nums1, int m, int* nums2, int n) {
    // right shift n
    int i = 0;
    int j = 0;
    int k = 0;
    for(i = m - 1; i >= 0; i --){
        nums1[i + n] = nums1[i];
    }
    i = n;
    j = 0;
    while(i < m + n && j < n){
        if(nums1[i] <= nums2[j]){
            nums1[k++] = nums1[i];
            i ++;
        } else {
            nums1[k++] = nums2[j];
            j ++;
        }
    }
    while(j < n){
        nums1[k++] = nums2[j];
        j ++;
    }
}