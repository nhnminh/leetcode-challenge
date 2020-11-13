"""
==== Populating Next Right Pointers in Each Node ====
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        current = root 
        leftmostChild = None
        
        while current.left:
            leftmostChild = current.left
            while current:
                current.left.next = current.right
                current.right.next = current.next.left if current.next else None 
                current = current.next
            current = leftmostChild
        
        return root