'''
Date: 2021-11-16 17:05:49
LastEditors: Chenhuiyu
LastEditTime: 2021-11-16 17:05:50
FilePath: \\.leetcode\\333.最大BST子树.py
'''
'''
给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小。其中，最大指的是子树节点数最多的。

二叉搜索树（BST）中的所有节点都具备以下属性：

左子树的值小于其父（根）节点的值。

右子树的值大于其父（根）节点的值。

注意:

子树必须包含其所有后代。
 

示例 1：
输入：root = [10,5,15,1,8,null,7]
输出：3
解释：本例中最大的 BST 子树是高亮显示的子树。返回值是子树的大小，即 3 。
示例 2：

输入：root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
输出：2
 

提示：
树上节点数目的范围是 [0, 10^4]
-10^4 <= Node.val <= 10^4
 

进阶:  你能想出 O(n) 时间复杂度的解法吗？
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def loopInfo(root):
            # 以root为根的子树返回四个信息：最大BST子树的大小、是否是搜索二叉树，整棵树的最大值、整棵树的最小值
            if root is None:
                return 0, True, float("-inf"), float("inf")
            left_bst_size, left_isBST, left_max, left_min = loopInfo(root.left)
            right_bst_size, right_isBST, right_max, right_min = loopInfo(root.right)

            # 判断当前root子树是否是搜索二叉树
            # 条件：左子树是搜索二叉树，右子树是搜索二叉树，左子树最大值小于root.val，右子树最小值大于root.val
            if left_isBST is True and right_isBST is True and left_max < root.val and right_min > root.val:
                root_isBst = True
            else:
                root_isBst = False

            # 更新以root为根的子树的最大值
            root_max = max(root.val, left_max, right_max)
            # 更新以root为根的子树的最小值
            root_min = min(root.val, left_min, right_min)

            # 以root为根的子树最大BST子树的大小
            if root_isBst == True:
                # 左子树整体都是BST，左子树的节点个数就是left_bst_size，右子树同理
                root_bst_size = left_bst_size + right_bst_size + 1
            else:
                root_bst_size = max(left_bst_size, right_bst_size)
            return root_bst_size, root_isBst, root_max, root_min

        return loopInfo(root)[0]