// title: lowest-common-ancestor-of-a-binary-search-tree
// detail: https://leetcode.com/submissions/detail/195661780/
// datetime: Tue Dec 18 10:00:01 2018
// runtime: 20 ms
// memory: 6.4 MB

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode *node, *node_q, *prev;
    if(root == NULL){
        return NULL;
    }
    node = root;
    while( 1 ){
        if(p->val < node->val && q->val < node->val){
            node = node->left;
        } else if (p->val > node->val && q->val > node->val){
            node = node->right;
        } else {
            return node;
        }
    }
}