// title: pow(x,-n)
// detail: https://leetcode.com/submissions/detail/190608394/
// datetime: Tue Nov 20 09:52:38 2018
// runtime: 4 ms
// memory: N/A

double myPow(double x, int n) {
    if(n == 0){
        return 1;
    }
    if(n == 1){
        return x;
    }
    int i = 0;
    double result = 1;
    int pos = 1;
    if(n < 0){
        if(n == -2147483648){
            n = 2147483647;
            pos = -1;
        } else{
            n = -n;
            pos = 0;
        }
        
    }
    int half_n = n / 2;
    int r = n - 2 * half_n;
    result = myPow(x, half_n) * myPow(x, half_n);
    if(r){
        result *= x;
    }
    if(pos == 0){
        result = 1 / result;     
    } else if(pos == -1){
        result = 1 / (result * x);
    }
    return result;
}