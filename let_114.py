# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def modify(node: TreeNode):
            if not node:
                return
            _node_left = node.left
            _node_right = node.right

            if _node_left != None:
                node_root = modify(_node_left)
                node.right = node_root
                node.left = None

                if _node_right != None:
                    _right = node.right
                    while(_right.right != None):
                        _right = _right.right
                    _right.right = modify(_node_right)
            elif _node_right!= None:
                node.right = modify(_node_right)
                node.left = None

            return node

        modify(root)