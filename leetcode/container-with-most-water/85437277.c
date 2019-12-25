// title: container-with-most-water
// detail: https://leetcode.com/submissions/detail/85437277/
// datetime: Mon Dec 12 17:23:31 2016
// runtime: 9 ms
// memory: N/A

int maxArea(int* height, int heightSize) {
    int width;
    int h;
    int max_area = 0;
    int area;
    int i;
    int* l = height;
    int* r = height + heightSize - 1;
    while(l < r){
        width = r - l;
        h = (*l > *r ? *r : *l);
        area = width * h;
        if(area > max_area){
            max_area = area;
        }
        while(*l <= h){
            l ++;
        }
        while(*r <= h){
            r --;
        }
    }
    return max_area;
}