// title: house-robber-iii
// detail: https://leetcode.com/submissions/detail/59021534/
// datetime: Thu Apr 14 18:53:43 2016
// runtime: 592 ms
// memory: N/A

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int rob(TreeNode root) {
        if(root == null){
            return 0;
        }
        int money1 = 0;
        int money2 = root.val;
        if(root.left != null){
            money1 += rob(root.left);
            if(root.left.left != null){
                money2 += rob(root.left.left);
            }
            if(root.left.right != null){
                money2 += rob(root.left.right);
            }
        }
        if(root.right != null){
            money1 += rob(root.right);
            if(root.right.left != null){
                money2 += rob(root.right.left);
            }
            if(root.right.right != null){
                money2 += rob(root.right.right);
            }
        }
        if(money1 > money2){
            return money1;
        }
        return money2;
    }
}