from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.post_index = len(postorder) - 1

        def build(in_start: int, in_end: int):
            if in_start > in_end:
                return None
            
            root = TreeNode(postorder[self.post_index])
            self.post_index -= 1
            root.right = build(inorder.index(root.val) + 1, in_end)
            root.left = build(in_start, inorder.index(root.val) - 1)
            return root
        
        print(self.post_index)
        return build(0, len(inorder) - 1)

def main():
    sol = Solution()
    print(sol.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))

if __name__ == '__main__':
    main()