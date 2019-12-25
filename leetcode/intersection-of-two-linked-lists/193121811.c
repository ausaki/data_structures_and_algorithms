// title: intersection-of-two-linked-lists
// detail: https://leetcode.com/submissions/detail/193121811/
// datetime: Mon Dec  3 18:29:58 2018
// runtime: 12 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *node = NULL, *shorter = NULL, *longer = NULL;
    int lenA = 0, lenB = 0, diff = 0;
    shorter = headA;
    longer = headB;
    while(shorter || longer){
        if(shorter){
            lenA += 1;   
            shorter = shorter->next;
        }
        if(longer){
            lenB += 1;   
            longer = longer->next;
        }
        
    }
    if(lenA > lenB){
        shorter = headB;
        longer = headA;
        diff = lenA - lenB;
    }else{
        shorter = headA;
        longer = headB;
        diff = lenB - lenA;
    }
    while(diff){
        longer = longer->next;
        diff --;
    }
    while(longer && longer != shorter){
        longer = longer->next;
        shorter = shorter->next;
    }
    if(longer){
        return longer;
    }
    return NULL;
}