# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def walk(node: TreeNode, level: int):
            if level > len(result):
                result.append([])
            result[level-1].append(node.val)
            if node.left:
                walk(node.left, level+1)
            if node.right:
                walk(node.right, level+1)
        if root:
            walk(root, 1)
        return result