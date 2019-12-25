// title: rotate-array
// detail: https://leetcode.com/submissions/detail/193314368/
// datetime: Tue Dec  4 18:49:56 2018
// runtime: 8 ms
// memory: 1.4 MB

void rotate(int* nums, int numsSize, int k) {
    int i, j, tmp, count = 0, current, start, next, prev;
    k = k % numsSize;
    for(i = 0; count < numsSize; i++){
        start = i;
        current = start;
        prev = nums[current];
        do {
            next = (current + k) % numsSize;
            tmp = nums[next];
            nums[next] = prev;
            current = next;
            prev = tmp;
            count ++;
        } while(start != current);
    }
}