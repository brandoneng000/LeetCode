import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root: TreeNode):
            if not root:
                return []
            
            if not root.left and not root.right:
                return [1]
            
            left = dfs(root.left)
            right = dfs(root.right)

            for dist_left in left:
                for dist_right in right:
                    if dist_left + dist_right <= distance:
                        self.res += 1
            
            return [dist + 1 for dist in left + right if dist < distance]

        self.res = 0
        dfs(root)
        return self.res