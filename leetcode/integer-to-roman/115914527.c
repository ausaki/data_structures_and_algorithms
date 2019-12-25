// title: integer-to-roman
// detail: https://leetcode.com/submissions/detail/115914527/
// datetime: Mon Aug 28 16:40:15 2017
// runtime: 79 ms
// memory: N/A

char* intToRoman(int num) {
    int roman[] = {1, 5, 10, 50, 100, 500, 1000, 4000};
    char chars[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    char* result = (char*)malloc(20);  
    int i, k=0, l, r, m;
    i = 3;
    
    
    while(num > 0){
        l = 0;
        r = 7;
        while(l < r){
            m = l + (r - l) / 2;
            if(num > roman[m]){
                l = m + 1;
            } else if(num == roman[m]){
                l = r = m;
            } else {
                r = m - 1;
            }
        }
        
        if(num >= roman[l]){
            i = l;
            l = roman[i];
            r = roman[i + 1];
            
        } else {
            i = l - 1;
            l = roman[i];
            r = roman[i + 1];
        }
        if(num >= l && num < r){
            if(l == 1 || l == 10 || l == 100){
                if(r - l <= num){
                    result[k++] = chars[i];
                    result[k++] = chars[i + 1];
                    num -= r - l; 
                } else {
                    result[k++] = chars[i];
                    num -= l;
                }
            } else if((roman[i - 1] == 1 || roman[i - 1] == 10 || roman[i - 1] == 100) && r - roman[i - 1] <= num){
                result[k++] = chars[i - 1];
                result[k++] = chars[i + 1];
                num -= r - roman[i - 1]; 
            } else {
                result[k++] = chars[i];
                num -= l;
            }
        }
       // for(i = 0; i < 7; i ++){
       //      l = roman[i];
       //      r = roman[i + 1];
       //      if(num >= l && num < r){
       //          if(l == 1 || l == 10 || l == 100){
       //              if(r - l <= num){
       //                  result[k++] = chars[i];
       //                  result[k++] = chars[i + 1];
       //                  num -= r - l; 
       //              } else {
       //                  result[k++] = chars[i];
       //                  num -= l;
       //              }
       //          } else if((roman[i - 1] == 1 || roman[i - 1] == 10 || roman[i - 1] == 100) && r - roman[i - 1] <= num){
       //              result[k++] = chars[i - 1];
       //              result[k++] = chars[i + 1];
       //              num -= r - roman[i - 1]; 
       //          } else {
       //              result[k++] = chars[i];
       //              num -= l;
       //          }
       //          break;
       //      }
       //  }
    }
    result[k] = 0;
    return result;
}