from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.cache = {}
        self.most_freq = 0
        def dfs(root: TreeNode):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            cur_sum = left + right + root.val
            self.cache[cur_sum] = self.cache.get(cur_sum, 0) + 1
            self.most_freq = max(self.most_freq, self.cache[cur_sum])
            return cur_sum

        dfs(root)
        return [key for key in self.cache if self.cache[key] == self.most_freq]
