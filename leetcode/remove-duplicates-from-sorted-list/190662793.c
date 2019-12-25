// title: remove-duplicates-from-sorted-list
// detail: https://leetcode.com/submissions/detail/190662793/
// datetime: Tue Nov 20 14:25:59 2018
// runtime: 4 ms
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
    int val = NULL;
    struct ListNode* node = head;
    struct ListNode* prev = head;
    while(node){
        if(node->val == val){
            prev->next = node->next;
        } else {
            prev = node;
            val = node->val;
        }
        node = node->next;
    }
    return head;
}