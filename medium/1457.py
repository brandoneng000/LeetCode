from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = set()

        def dfs(root: TreeNode):
            if not root.left and not root.right:
                if root.val in count:
                    return int(len(count - {root.val}) <= 1)
                else:
                    return int(len(count) + 1 <= 1)
            
            if root.val in count:
                count.remove(root.val)
            else:
                count.add(root.val)
            
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0

            if root.val in count:
                count.remove(root.val)
            else:
                count.add(root.val)
            
            return left + right

        return dfs(root)

    # def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    #     count = collections.Counter()

    #     def dfs(root: TreeNode):
    #         if not root.left and not root.right:
    #             count[root.val] += 1
    #             res = sum(count[key] % 2 for key in count) <= 1
    #             count[root.val] -= 1
    #             return int(res)
            
    #         count[root.val] += 1
    #         left = dfs(root.left) if root.left else 0
    #         right = dfs(root.right) if root.right else 0
    #         count[root.val] -= 1

    #         return left + right
        
    #     return dfs(root)