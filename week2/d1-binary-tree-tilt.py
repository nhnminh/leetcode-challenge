# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
    #Init 
    total_tilt = 0
    def valueSum(node):
        nonlocal total_tilt
        if node is None:
            return 0
        else:
            resLeft = valueSum(node.left)
            resRight = valueSum(node.right)
            tilt = abs(resLeft - resRight)
            total_tilt += tilt

        return resLeft + resRight + node.val  
    
    valueSum(root)
    return total_tilt