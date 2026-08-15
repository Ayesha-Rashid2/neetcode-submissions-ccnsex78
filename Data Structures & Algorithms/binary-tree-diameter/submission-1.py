# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #set a max dia and a normal dia
        # stop the path when a node doesn't have a left or right

        global max_diamater
        max_diamater = 0

        def dfs(root):
            global max_diamater
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = left + right

            max_diamater = max(max_diamater, diameter)

            return 1 + max(left, right)

        dfs(root)

        return max_diamater

       


        