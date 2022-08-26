# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = {"value": -inf}

        def walk(node: TreeNode):
            left_value = 0
            right_value = 0
            if node.left != None:
                left_value = max(0, walk(node.left))

            if node.right != None:
                right_value = max(0, walk(node.right))

            max_value = node.val + left_value + right_value

            if max_value > result["value"]:
                result["value"] = max_value

            return max(node.val, node.val + left_value, node.val + right_value)

        walk(root)

        return result["value"]