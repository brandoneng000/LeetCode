from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def tree_branches(start: int, end: int) -> List[TreeNode]:
            res = []

            if start > end:
                res.append(None)
                return res
            
            for n in range(start, end + 1):
                left_branches = tree_branches(start, n - 1)
                right_branches = tree_branches(n + 1, end)

                for left in left_branches:
                    for right in right_branches:
                        root = TreeNode(n)
                        root.left = left
                        root.right = right
                        res.append(root)
            
            return res
        
        if n == 0:
            return []
        return tree_branches(1, n)

def main():
    sol = Solution()
    print(sol.generateTrees(3))
    print(sol.generateTrees(1))

if __name__ == '__main__':
    main()