// title: intersection-of-two-linked-lists
// detail: https://leetcode.com/submissions/detail/193121493/
// datetime: Mon Dec  3 18:25:14 2018
// runtime: 16 ms
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
    node = headA;
    while(node){
        lenA += 1;
        node = node->next;
    }
    node = headB;
    while(node){
        lenB += 1;
        node = node->next;
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