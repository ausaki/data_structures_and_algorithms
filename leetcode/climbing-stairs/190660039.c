// title: climbing-stairs
// detail: https://leetcode.com/submissions/detail/190660039/
// datetime: Tue Nov 20 14:12:49 2018
// runtime: 0 ms
// memory: N/A

int climbStairs(int n) {
    int a = 1, b = 1, t;
    while(n--){
        t = a + b;
        a = b;
        b = t;
    }
    return a;
}