from hashlib import new
from tkinter.tix import Tree
from typing import List, Optional
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, TreeNode):
            return False

        return self.val == __o.val and self.left == __o.left and self.right == __o.right


class Solution:
    def allPossibleFBT(self, n: int, mem={1: [TreeNode()]}) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        else:
            if n not in mem:
                ans = []
                for i in range(1, n, 2):
                    j = n - i - 1
                    for all_left in self.allPossibleFBT(i):
                        for all_right in self.allPossibleFBT(j):
                            t = TreeNode()
                            t.left = all_left
                            t.right = all_right
                            ans.append(t)

                mem[n] = ans

            return mem[n]


if __name__ == '__main__':
    ss = Solution()

    s3 = ss.allPossibleFBT(3)
    e3 = [TreeNode(0, TreeNode(), TreeNode())]
    assert e3 == s3

    s7 = ss.allPossibleFBT(7)
    e7 = [
        TreeNode(0, TreeNode(0, TreeNode(), TreeNode()),
                 TreeNode(0, TreeNode(), TreeNode())),
        TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(),
                 TreeNode()), TreeNode()), TreeNode()),
        TreeNode(0, TreeNode(0, TreeNode(), TreeNode(
            0, TreeNode(), TreeNode())), TreeNode()),
        TreeNode(0, TreeNode(), TreeNode(0, TreeNode(),
                 TreeNode(0, TreeNode(), TreeNode()))),
        TreeNode(0, TreeNode(), TreeNode(0, TreeNode(
            0, TreeNode(), TreeNode()), TreeNode()))
    ]

    assert all(i7 in e7 for i7 in s7)
    assert all(i7 in s7 for i7 in e7)
