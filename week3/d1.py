# Range sum of BST 
# Given the root node of a binary search tree, 
# return the sum of values of all nodes with a 
# value in the range [low, high].
# ===================================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        if(root.val <= high and root.val >= low):
            # print("Count " + str(root.val))
            sumCond = root.val
        else: 
            sumCond = 0
            
        if(root.left is not None):
            # print("Go left " + str(root.left.val))
            sumCond += self.rangeSumBST(root.left, low, high)
        if(root.right is not None): 
            # print("Go right " + str(root.right.val))
            sumCond += self.rangeSumBST(root.right, low, high)
            
        return sumCond

class SolutionOptimized:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if(root.val <= high and root.val >= low):
            sumVal = root.val
        else:
            sumVal = 0
        if root.val > high :
            sumVal += self.rangeSumBST(root.left, low, high)
        if root.val < low : 
            sumVal += self.rangeSumBST(root.right, low, high)
        
        return sumVal

    