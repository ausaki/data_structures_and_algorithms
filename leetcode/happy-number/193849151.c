// title: happy-number
// detail: https://leetcode.com/submissions/detail/193849151/
// datetime: Fri Dec  7 17:15:09 2018
// runtime: 0 ms
// memory: 778.2 KB

int squre_sum(int n){
    int sum = 0, r;
    while(n){
        r = n % 10;
        n = n / 10;
        sum += r * r;
    }
    return sum;
}
bool isHappy(int n) {
    // 快慢指针解法，参考https://leetcode.com/problems/linked-list-cycle-ii/
    int ni = n, nj = n;
    do{
        ni = squre_sum(ni);
        nj = squre_sum(squre_sum(nj));
        if(nj == 1){
            return true;
        }
    }while(ni != nj);
    return false;
}