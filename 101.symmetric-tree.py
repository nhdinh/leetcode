# 101. Symmetric Tree

from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def checkMirrored(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False
            
            return left.val == right.val and checkMirrored(left.left, right.right) and checkMirrored(left.right, right.left)
        
        return checkMirrored(root.left, root.right)