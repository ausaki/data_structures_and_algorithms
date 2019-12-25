// title: delete-node-in-a-linked-list
// detail: https://leetcode.com/submissions/detail/195669520/
// datetime: Tue Dec 18 10:43:58 2018
// runtime: 4 ms
// memory: 868.4 KB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode *prev;
    while(node->next){
        node->val = node->next->val;
        prev = node;
        node = node->next;
    }
    prev->next = NULL;
}