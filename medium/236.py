from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def dfs(root: TreeNode, find: TreeNode, found_list: List[TreeNode]):
        #     if not root:
        #         return False
        #     if root == find:
        #         found_list.append(root)
        #         return True
        #     if dfs(root.left, find, found_list):
        #         found_list.append(root)
        #         return True
        #     if dfs(root.right, find, found_list):
        #         found_list.append(root)
        #         return True
            
        #     return False
        # found_q = []
        # found_p = []
        # dfs(root, p, found_p)
        # dfs(root, q, found_q)
        # found_q = found_q[::-1]
        # found_p = found_p[::-1]
        # print([p.val for p in found_p])
        # print([q.val for q in found_q])

        # for index in range(min(len(found_p), len(found_q))):
        #     if found_q[index] != found_p[index]:
        #         return found_p[index - 1]
        #     if index == min(len(found_p), len(found_q)) - 1:
        #         return found_p[index]

        # return root
        self.ans = None
        def dfs(root: TreeNode):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)

            mid = root == p or root == q

            if mid + left + right >= 2:
                self.ans = root
            
            return mid or left or right
        
        dfs(root)
        return self.ans