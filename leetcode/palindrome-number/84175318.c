// title: palindrome-number
// detail: https://leetcode.com/submissions/detail/84175318/
// datetime: Tue Nov 29 16:10:15 2016
// runtime: 85 ms
// memory: N/A

bool isPalindrome(int x) {
    int MAX_INT = 2147483647;
    int x_value = x;
    int reversed_x = 0;
    int tmp = 0;
    int r = 0;
    if(x < 0){
        return false;
    }
    while((tmp = x_value / 10) != 0){
        r = x_value % 10;
        if(reversed_x > MAX_INT - r){
            return false;
        }
        reversed_x += r;
        if(reversed_x > MAX_INT / 10){
            return false;
        }
        reversed_x *= 10;
        x_value = tmp;
    }
    if(reversed_x > MAX_INT - x_value){
        return false;
    }
    reversed_x += x_value;
    return reversed_x == x;
}