// title: min-stack
// detail: https://leetcode.com/submissions/detail/193115348/
// datetime: Mon Dec  3 17:16:52 2018
// runtime: 56 ms
// memory: N/A

typedef struct {
    int size;
    int top;
    int* buffer;
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack *ms = (MinStack*)malloc(sizeof(MinStack));
    ms->size = maxSize;
    ms->buffer = (int*)malloc(sizeof(int) * ms->size);
    ms->top = 0;
    return ms;
}

void minStackPush(MinStack* obj, int x) {
    // if(obj->top == obj->size){
    //     return NULL;
    // }
    obj->buffer[obj->top++] = x;
    // return NULL;
}

void minStackPop(MinStack* obj) {
    // if(obj->top == 0){
    //     return NULL;
    // }
    obj->top--;
}

int minStackTop(MinStack* obj) {
    if(obj->top == 0){
        return -1;
    }
    return obj->buffer[obj->top - 1];
}

int minStackGetMin(MinStack* obj) {
    int i = 0;
    int min = obj->buffer[0];
    for(i = 1; i < obj->top; i++){
        if(obj->buffer[i] < min){
            min = obj->buffer[i];
        }
    }
    return min;
}

void minStackFree(MinStack* obj) {
    free(obj->buffer);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */