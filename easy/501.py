from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # self.res = []
        # self.cache = {}

        # def dfs(root: TreeNode):
        #     if not root:
        #         return
            
        #     self.cache[root.val] = self.cache.get(root.val, 0) + 1
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        # mode = max(self.cache.values())
        # return [key for key in self.cache if self.cache[key] == mode]

        self.res = []
        self.mode = 0
        self.max_mode = 1
        self.cur_val = root.val

        def find_mode_val(root: TreeNode):
            if not root:
                return
            
            find_mode_val(root.left)
            if self.cur_val == root.val:
                self.mode += 1
                self.max_mode = max(self.mode, self.max_mode)
            else:
                self.cur_val = root.val
                self.mode = 1
            find_mode_val(root.right)

        
        def find_modes(root: TreeNode):
            if not root:
                return
            
            find_modes(root.left)
            if self.cur_val == root.val:
                self.mode += 1
                if self.mode == self.max_mode:
                    self.res.append(self.cur_val)
            else:
                self.cur_val = root.val
                self.mode = 1
                if self.mode == self.max_mode:
                    self.res.append(self.cur_val)
            find_modes(root.right)
            
                

        find_mode_val(root)
        self.mode = 0
        self.cur_val = root.val
        find_modes(root)
        return self.res