# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = collections.deque([root])

        while q:
            q_len = len(q)
            sub_res = []

            for i in range(q_len):
                node = q.popleft()
                sub_res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(sub_res)

        return res




        
        










        
        '''
        queue = deque([root])
        result_list = []

        while queue:
            qLen = len(queue)
            level = []

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        
            result_list.append(level)

        return result_list[:-1]

        '''

        