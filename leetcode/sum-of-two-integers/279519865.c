// title: sum-of-two-integers
// detail: https://leetcode.com/submissions/detail/279519865/
// datetime: Sun Nov 17 19:02:37 2019
// runtime: 0 ms
// memory: 6.8 MB



int getSum(int a, int b){
    unsigned int s = a;
    unsigned int c = b;
    unsigned int tmp;
    while(c != 0){
        tmp = s ^ c;
        c = (s & c) << 1;
        s = tmp;
    }
    return (int)s;
}

