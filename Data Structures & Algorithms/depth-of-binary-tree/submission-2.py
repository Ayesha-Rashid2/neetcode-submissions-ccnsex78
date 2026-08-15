# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        stack = [[root, 1]]

        if not root:
            return max_level

        while stack:
            node, level = stack.pop()
            max_level = max(max_level, level)

            if node.left:
                stack.append([node.left, level+1])
            if node.right:
                stack.append([node.right, level+1])
            
           
            
        
        return max_level












        ''' Recurisve DFS
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

     
        if not root:
            return 0

        level = 0

        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return level
        '''


