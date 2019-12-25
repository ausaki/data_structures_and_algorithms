// title: pow(x,-n)
// detail: https://leetcode.com/submissions/detail/190613743/
// datetime: Tue Nov 20 10:21:33 2018
// runtime: 4 ms
// memory: N/A

double myPow(double x, int n) {
    if(n == 0){
        return 1;
    }
    double result = 1;
    int pos = 1;
    if(n < 0){
        n = -(n + 1);
        pos = 0;
    }
    int half_n = n / 2;
    int r = n - 2 * half_n;
    result = myPow(x, half_n);
    result *= result;
    if(r){
        result *= x;
    }
    if(pos == 0){
        result *= x;     
        result = 1 / result;
    }
    return result;
}