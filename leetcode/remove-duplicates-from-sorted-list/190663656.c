// title: remove-duplicates-from-sorted-list
// detail: https://leetcode.com/submissions/detail/190663656/
// datetime: Tue Nov 20 14:30:01 2018
// runtime: 0 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head == NULL){
        return NULL;
    }
    struct ListNode* prev = head;
    struct ListNode* node = head->next;
    while(node){
        if(node->val == prev->val){
            prev->next = node->next;
        } else {
            prev = node;
        }
        node = node->next;
    }
    return head;
}