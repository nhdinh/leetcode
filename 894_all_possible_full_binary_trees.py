from operator import le
from typing import List, Optional
from copy import copy

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int, nodes={}) -> List[Optional[TreeNode]]:
        def getLeaf(_node: TreeNode, _leaves=[]):
            if _node is None:
                return None
            if _node.left is not None:
                _leaves.append(getLeaf(_node.left, _leaves))
            if _node.right is not None:
                _leaves.append(getLeaf(_node.right, _leaves))
            if _node.left is None and _node.right is None:
                _leaves.append(_node)

            return _leaves

        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode()]
        else:
            if n not in nodes:
                nodes[n] = []
                prev_node = self.allPossibleFBT(n-2, nodes)


if __name__ == '__main__':
    ss = Solution()

    # print([TreeNode()])

    # t0 = TreeNode()
    # t0.left = TreeNode()
    # t0.right = TreeNode()
    # t0.right.left = TreeNode()
    # t0.right.right = TreeNode()
    # t0.right.right.left = TreeNode()
    # t0.right.right.right = TreeNode()
    # print([t0])

    # s0 = ss.allPossibleFBT(1)
    # print(set(s0) == set([[0]]))

    s2 = ss.allPossibleFBT(3)
    # print(set(s2)==set([[0,0,0]]))

    # s1 = ss.allPossibleFBT(7)
    # print(set(s1)==set([[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]]))
