// title: intersection-of-two-linked-lists
// detail: https://leetcode.com/submissions/detail/193118552/
// datetime: Mon Dec  3 17:48:00 2018
// runtime: 592 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *node = NULL;
    while(headB){
        node = headA;
        while(node){
            if(node == headB){
                return node;
            }
            node = node->next;
        }
        headB = headB->next;
    }
    return NULL;
}