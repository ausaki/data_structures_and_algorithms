// title: median-of-two-sorted-arrays
// detail: https://leetcode.com/submissions/detail/76378411/
// datetime: Thu Sep 29 23:40:14 2016
// runtime: 26 ms
// memory: N/A

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int isOdd = (nums1Size + nums2Size) % 2;
    int medianIndex = (nums1Size + nums2Size) / 2;
    double median = 0;
    int prevValue = 0;
    int i, j;
    i = j = 0;
    while(i < nums1Size && j < nums2Size){
        if(nums1[i] < nums2[j]){
            if(i + j  == medianIndex){
                median = isOdd ? nums1[i] : (nums1[i] + prevValue) / 2.0;
                break;
            } else {
                prevValue = nums1[i];
                i ++;
            }
        } else {
            if(i + j  == medianIndex){
                median = isOdd ? nums2[j] : (nums2[j] + prevValue) / 2.0;
                break;
            } else {
                prevValue = nums2[j];
                j ++;
            }
        }
    }
    if(i == nums1Size){
        while(j < nums2Size){
            if(i + j  == medianIndex){
                median = isOdd ? nums2[j] : (nums2[j] + prevValue) / 2.0;
                break;
            } else {
                prevValue = nums2[j];
                j ++;
            }
        }
    } else if(j == nums2Size){
        while(i < nums1Size){
            if(i + j  == medianIndex){
                median = isOdd ? nums1[i] : (nums1[i] + prevValue) / 2.0;
                break;
            } else {
                prevValue = nums1[i];
                i ++;
            }
        }
    }
    return median;
}