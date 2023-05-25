from typing import List, Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cache = {}
        count_cache = collections.defaultdict(int)
        res = []

        def helper(root: TreeNode):
            if not root:
                return 0
            
            tree = (helper(root.left), root.val, (helper(root.right)))
            if tree not in cache:
                cache[tree] = len(cache) + 1
            id = cache[tree]
            count_cache[id] += 1
            if count_cache[id] == 2:
                res.append(root)

            return id

        helper(root)
        return res
