#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,preorder,preStart,preEnd,inorder,inStart,inEnd):
        # base case
        if preStart>preEnd:
            return None
        # 前序遍历的第一个原始是头结点的值
        rootVal=preorder[preStart]
        # 找到头结点在中序遍历中的位置
        rootIndex=inorder.index(rootVal)
        # 建立头结点
        root=TreeNode(rootVal)
        # 递归创建左子树
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
# @lc code=end

