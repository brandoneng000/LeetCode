import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def dfs(root, vals, find, level):
        #     if not root:
        #         return False
        #     if root == find:
        #         vals.append((root, level))
        #         return True
            
        #     if dfs(root.left, vals, find, level + 1):
        #         vals.append((root, level))
        #         return True
        #     if dfs(root.right, vals, find, level + 1):
        #         vals.append((root, level))
        #         return True
        #     return False
        
        # vals_p = []
        # dfs(root, vals_p, p, 0)

        # vals_q = []
        # dfs(root, vals_q, q, 0)

        # vals = collections.Counter(vals_q + vals_p)
        # res = (TreeNode(float('inf')), -1)
        # for val in vals:
        #     if vals[val] == 2:
        #         if val[1] > res[1]:
        #             res = val
        
        # return res

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root